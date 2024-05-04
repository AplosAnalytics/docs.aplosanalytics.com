# SAS Program
The SAS program uses functions to interact with Aplos NCA to analyze data. Each of the functions are shown and described below. Code chunks look best in Dark mode. You can make the change at the top right of your browser.

## Setup global variables
This section of code sets up global variables to be used in the SAS code. It also imports the security information to be used to acquire the JSON Web Token. 

```sas:line-numbers
/* Setting some Global variables that are used throughout the process */
%global execution_id;
%global authorization;
%global APLOS_API_URL;
%global id_token;
%global key_value;
%global presigned_url;
%global x_amz_algorithm;
%global x_amz_credential;
%global x_amz_date;
%global x_amz_security_token;
%global policy_value;
%global x_amz_signature;
%global bucket_name;
%global object_key;
%global file_name;
%global download_url;

/* environment file with env variables that we will create macro variables from */
filename envfile '/<directory>/sas_security.env';

/* set the environment macro variables from the environment file */
data _null_;
    infile envfile;
    input;
    length key $32 value $100;  /* Adjust lengths as needed */
    
    /* Find the position of the equals sign */
    pos = index(_infile_, '=');
    if pos > 0 then do;
        /* Split the string into key and value */
        key = substr(_infile_, 1, pos-1);
        value = substr(_infile_, pos+1);

        /* Trim any whitespace */
        key = strip(key);
        value = strip(value);

        /* Create macro variables */
        call symputx(key, value);
    end;
run;
```

## Get JSON Web Token 
This function uses 4 pieces of information to acquire a jwt from Amazon Cognito. These are the client identifier (`COGNITO_CLIENT_ID`), username (`COGNITO_USER_NAME`), password (`COGNITO_PASSWORD`), and region (`COGNITO_REGION`). The client identifier and region are available from the web interface under [Profile | API Configuration](./sas-overview.md#security-information).

```sas:line-numbers
%macro get_jwt;
	%let login_url="https://cognito-idp.&COGNITO_REGION..amazonaws.com/";
	%put Login Url: &login_url;

	filename authresp temp;
	filename authbody temp;
	
	proc json out=authbody nosastags;
	    write values "AuthFlow" "USER_PASSWORD_AUTH";
	    write values "AuthParameters";
	    write open object;
	    write values "USERNAME" "&COGNITO_USER_NAME";
	    write values "PASSWORD" "&COGNITO_PASSWORD";
	    write close;
	    write values "ClientId" "&COGNITO_CLIENT_ID";
	    write values "method_type" "post";
	run;
	
	data _null_;
	    infile authbody;
	    input;
	    put _infile_;
	run;
	
	proc http
	    url=&login_url
	    method="POST"
	    in=authbody
	    out=authresp;
	    headers
	    "Content-Type"="application/x-amz-json-1.1"
	    "X-Amz-Target"="AWSCognitoIdentityProviderService.InitiateAuth";
	run;
	
	/* debug: print the response from authentication call */
	data _null_;
	    infile authresp;
	    input;
	    put _infile_;
	run;
	
	libname resp_tok json fileref=authresp;
	
	data _null_;
	    set resp_tok.AuthenticationResult;
	    if _N_ = 1;  /* Assumes 'AccessToken' is in the first record of the dataset */
	    call symputx('id_token', IdToken);
	run;
	
	/* debug: print the access token */
	%put &id_token;
%mend;
```

## Acquire URL for file upload 
This function requests the secure URL to which you will upload the input data file. This function uses 3 pieces of information to acquire the upload URL. These are the input file name (`file_path` and `file_name`), URL for the API (`APLOS_API_URL`), and jwt (`id_token`). The URL for the API is available from the web interface under [Profile | API Configuration](./sas-overview.md#security-information).

```sas:line-numbers
%macro get_upload_url;
	%let file_path = "/<directory>/single_ev_10.csv";
	%let file_name = %scan(&file_path, -1, "/");
	%put &file_name;
	
	filename in_file &file_path;
	filename upresp temp;
	filename upbody temp;
	
	proc json out=upbody nosastags;
	    write values "file_name" "&file_name";
	    write values "method_type" "post";
	run;
	
	%let upload_url = %sysfunc(catt(&APLOS_API_URL, /nca-engine/generate-upload-url));
	%let authorization = %sysfunc(catx(%str( ), Bearer, %unquote(&id_token)));
	%put &authorization;
	
	proc http
	    url="&upload_url"
	    method="POST"
	    in=upbody
	    out=upresp;
	    headers
	    "Content-Type"="application/json"
	    "Authorization"="&authorization";
	run;
	
	/* debug: print the response from upload call */
	data _null_;
	    infile upresp;
	    input;
	    put _infile_;
	run;
	
	libname pre_url json fileref=upresp;
	
	data _null_;
	    set pre_url.presigned;
	    call symputx('presigned_url', url);
	run;
	
	data _null_;
	    set pre_url.presigned_fields;
	    call symputx('key_value', key);
	    call symputx('x_amz_algorithm', x_amz_algorithm);
	    call symputx('x_amz_credential', x_amz_credential);
	    call symputx('x_amz_date', x_amz_date);
	    call symputx('x_amz_security_token', x_amz_security_token);
	    call symputx('policy_value', policy);
	    call symputx('x_amz_signature', x_amz_signature);
	run;
	
	data _null_;
	    set pre_url.s3;
	    call symputx('bucket_name', bucket_name);
	    call symputx('object_key', object_key);
	run;
	
	/* debug: print the variable values */
	%put &key_value;
	%put &presigned_url;
	%put &x_amz_algorithm;
	%put &x_amz_credential;
	%put &x_amz_date;
	%put &x_amz_security_token;
	%put &policy_value;
	%put &x_amz_signature;
%mend;

```

## Upload input data file 
This function uploads the data file for analysis using the secure URL. This function uses 2 pieces of information. These are the input file (`in_file`) and the secure URL (`presigned_url`). The response includes a security token that authenticates the user.

```sas:line-numbers
%macro upload_file_api;
	filename upload temp;
	
	/* There is no response from this request when the file is actually uploaded */
	/* in initial development of this script the response code is 204 no content but files are uploaded */
	proc http
		in=MULTI FORM (
		"key"=%unquote("&key_value"),
		"x-amz-algorithm"=%unquote("&x_amz_algorithm"),
		"x-amz-credential"=%unquote("&x_amz_credential"),
		"x-amz-date"=%unquote("&x_amz_date"),
		"x-amz-security-token"=%unquote("&x_amz_security_token"),
		"policy"=%unquote("&policy_value"),
		"x-amz-signature"=%unquote("&x_amz_signature"),
		"file" = in_file
		FILENAME="&file_name"
		)
	    url="&presigned_url"
	    ct="multipart/form-data"
	    method="POST"
	    out=upload;
	run;
%mend;

```

## Initiate Analysis 
This function initiates the analysis by Aplos NCA. This function uses the configuration settings (`confjson`) and meta data (`metajson`) and information from the prior upload function to intiate the analysis. The response from the secure URL request is used to identify the input analysis dataset location on the server for the anlaysis. The configuration settings and meta data must be list objects within R for this function to operate properly. The URL for the API is available from the web interface under [Profile | API Configuration](./sas-overview.md#security-information). 

```sas:line-numbers
%macro execute_analysis;
	filename exresp temp;
	filename exbody temp;
	filename confjson '/<directory>/configuration_single_ev.json';
	filename metajson '/<directory>/meta_data.json';
	
	
	data _null_;
	    length json_string $32767;
	    infile metajson lrecl=32767 truncover;
	    retain json_string '';
	    input temp_line $char32767.;
	    json_string = catx(' ', json_string, tranwrd(temp_line, '"', '%str(%")'));
	    call symputx('meta_data', json_string);
	run;
	
	data _null_;
	    length json_string $32767;
	    infile confjson lrecl=32767 truncover;
	    retain json_string '';
	    input temp_line $char32767.;
	    json_string = catx(' ', json_string, tranwrd(temp_line, '"', '%str(%")'));
	    call symputx('conf_data', json_string);
	run;
	
	%let execution_analysis_url = %sysfunc(catt(&APLOS_API_URL, /nca-engine/executions));
	%put &execution_analysis_url;
	
	proc json out=exbody nosastags;
	    write values "s3";
	    write open object;
	    write values "bucket_name" "&bucket_name";
	    write values "object_key" "&object_key";
	    write close;
	    write values "meta_data" "&meta_data";
	    write values "configuration" "&conf_data";
	run;
	
	proc http
	    url="&execution_analysis_url"
	    method="POST"
	    in=exbody
	    out=exresp;
	    headers
	    "Content-Type"="application/json"
	    "Authorization"="&authorization";
	run;
	
	data _null_;
	    infile exresp;
	    input;
	    put _infile_;
	run;
	
	libname ex_url json fileref=exresp;
	
	proc print data=ex_url.root;
	run;
	
	data _null_;
	    set ex_url.root;
	    call symputx('execution_id', execution_id);
	run;
	
	%put Execution ID: &execution_id;
%mend;

```

## Request Execution Status 
This function checks the status of the analysis, prints that status, and then returns the download URL when the analysis is complete. This function uses 3 pieces of information. These are the URL for the API (`APLOS_API_URL`), jwt (`authorization`) and the unique analysis identifier (`execution_id`). The URL for the API is available from the web interface under [Profile | API Configuration](./sas-overview.md#security-information), and the unique analysis identifier is available from the response from the API when you initiate an analysis. 

```sas:line-numbers
%macro execution_status;
    %let complete = 0;
    %let status = %str();
    %let elapsed = %str();
	%let execution_status_url = %sysfunc(catt(&APLOS_API_URL, /nca-engine/executions/, &execution_id));
	%put &execution_status_url;
	
    %do %while(&complete<1);
        /* Set up headers and perform the GET request */
        filename st_resp temp;
        proc http
		    url="&execution_status_url"
		    method="GET"
		    out=st_resp;
		    headers
		    "Content-Type"="application/json"
		    "Authorization"="&authorization";
		run;

        libname st_url json fileref=st_resp;
		
		data _null_;
		    set st_url.root;
		    call symputx('status', status);
		    call symputx('elapsed', elapsed);
		run;
		
        /* Check the status */
        %if &status = failed %then %do;
            %put Execution failed. Execution ID = &execution_id.;
            %goto exitloop;
        %end;
        %else %if &status = complete %then %do;
            %let complete = 1;
            %put Execution complete.;
            %put Execution duration = &elapsed.;
        %end;
        %else %do;
            %put Not yet complete ... &status.;
            data _null_; call sleep(4,1); run;
        %end;
    %end;
	
    %exitloop:
	
	libname st_url json fileref=st_resp;
	
	data _null_;
	    set st_url.presigned;
		call symputx('download_url', url);
	run;
	
	/* debug: print the download url */
    /* %put Download URL = &download_url; */
    
%mend;
```

## Download results
The final function downloads the results using the secure download URL (`download_url`) from the completed analysis request.

```sas:line-numbers
%macro download_results;
	filename inzip '/<directory>/results.zip';

	proc http
		url="&download_url"
		method="GET"
		out=inzip;
	run;
%mend;
```
## Run SAS Program
The SAS program can then be executed by running each function in order as shown below.

```sas:line-numbers
/* Run the functions in sequence */
%get_jwt;
%get_upload_url;
%upload_file_api;
%execute_analysis;
%execution_status;
%download_results;
```