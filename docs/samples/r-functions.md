# 2️⃣ R Functions
The R functions used for interacting with Aplos NCA to analyze data are shown and described below. 

## Get JSON Web Token 
This function uses 4 pieces of information to acquire a jwt from Amazon Cognito. These are the client identifier (`client_id`), username, password, and region. The client identifier and region are available from the web interface under [Profile | API Configuration](./r-script.md#security-information).

```r:line-numbers
get_jwt <- function(client_id, username, password, region){
  headers <- c("Content-Type" = "application/x-amz-json-1.1", 
               "X-Amz-Target" = "AWSCognitoIdentityProviderService.InitiateAuth")
  body <- list(
    AuthFlow="USER_PASSWORD_AUTH",
    AuthParameters=list("USERNAME"=username, "PASSWORD"=password),
    ClientId=client_id,
    method_type = "post"
  )
  
  response <- POST(url = paste0("https://cognito-idp.",region,".amazonaws.com/"),
                   add_headers(.headers = headers),
                   body = toJSON(body, auto_unbox = TRUE))
  
  result <- fromJSON(content(response, "text", encoding = "UTF-8"))
  jwt <- result$AuthenticationResult$IdToken
  return(jwt)
}
```

## Analysis with Aplos NCA
The function requires the following information:

  - JSON web token
  - Analysis dataset filename (and path)
  - Configuration in JSON format
  - Meta data in JSON format (optional)
  - Data cleaning rules in JSON format (optional)
  - Post processing rules in JSON format (optional)
  - API URL (The URL for the API is available from the web interface under [Profile | API Configuration](./r-script.md#security-information))
  - Folder for results file
  - Unzip (True/False)

### Acquire URL for file upload 
The following code requests the secure URL to which you will upload the input data file.

```r:line-numbers
  # Get pre-signed URL
  tenant_id <- decode_jwt(token)$payload$`custom:aplos_user_tenant_id`
  user_id <- decode_jwt(token)$payload$`custom:aplos_user_id`
  filename = str_split_i(input, "/", -1)
  upload_url = paste0(url,"/tenants/",tenant_id,"/users/",user_id,"/nca/files")
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  body <- list(
    "file_name"=filename,
    method_type = "post"
  )
  
  response <- POST(url = upload_url,
                   add_headers(.headers = headers),
                   body = toJSON(body, auto_unbox = TRUE))
  upload_url_result <- fromJSON(content(response, "text", encoding = "UTF-8"))
```

## Upload input data file 
This code uploads the data file for analysis using the secure URL. 

```r:line-numbers
  # Upload input file
  cat("Uploading input file ... \n")
  upload_url = upload_url_result$presigned$url
  headers <- c()
  body <- list(
    key = upload_url_result$presigned$fields$key,
    "x-amz-algorithm" = upload_url_result$presigned$fields$`x-amz-algorithm`,
    "x-amz-credential" = upload_url_result$presigned$fields$`x-amz-credential`,
    "x-amz-date" = upload_url_result$presigned$fields$`x-amz-date`,
    "x-amz-security-token" = upload_url_result$presigned$fields$`x-amz-security-token`,
    policy = upload_url_result$presigned$fields$policy,
    "x-amz-signature" = upload_url_result$presigned$fields$`x-amz-signature`,
    file = upload_file(normalizePath(input))
  )
  
  upload_response <- POST(url = upload_url, body = body)
```

## Initiate Analysis 
This code initiates the analysis by Aplos NCA.  

```r:line-numbers
  cat("Loading data cleaning configuration \n")
  clean_text <- paste(readLines(clean_file, warn = FALSE), collapse = "\n")
  
  cat("Loading analysis configuration \n")
  config_text <- paste(readLines(config_file, warn = FALSE), collapse = "\n")
  
  cat("Loading post processing configuration \n")
  post_text <- paste(readLines(post_file, warn = FALSE), collapse = "\n")
  
  cat("Loading analysis meta data \n")
  meta_text <- paste(readLines(meta_file, warn = FALSE), collapse = "\n")
  
  cat("Initiating analysis ... \n")
  cat("Initiating analysis ... \n")
  exec_id <- execute_analysis(result = upload_result, config = config_text,
                              meta = meta_text, clean = clean_text, post = post_text,
                              url = api_url, token = current.jwt)

  execute_analysis <- function(result,config,meta,clean,post,token,url){
  tenant_id <- decode_jwt(token)$payload$`custom:aplos_user_tenant_id`
  user_id <- decode_jwt(token)$payload$`custom:aplos_user_id`
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  # Build the body of the request
  payload <- sprintf(
    '{
    "file": {
      "id": "%s"
    },
    "configuration": %s,
    "meta_data": %s,
    "data_processing": %s,
    "post_processing": %s
  }',
    result$file$id,
    config,
    meta,
    clean,
    post
  )
  # save the body as a file
  write(payload, file = "payload.json")
  
  # Initiate the analysis
  response <- POST(url = paste0(url,"/tenants/",tenant_id,"/users/",user_id,"/nca/executions"),
                   add_headers(.headers = headers),
                   body = upload_file("payload.json"))
                   
  # Check the response
  if (http_status(response)$category == "Success") {
    cat("Execution initiated. \n")
  } else {
    cat("Error in the request. \n")
  }
  
  result <- fromJSON(content(response, "text", encoding = "UTF-8"))
  execution_id <- result$execution_id
  return(execution_id)
}
```

## Request Execution Status 
This code checks the status of the analysis, prints that status, and then returns the download URL when the analysis is complete. 

```r:line-numbers
  cat("Checking status ... \n")
  tenant_id <- decode_jwt(token)$payload$`custom:aplos_user_tenant_id`
  user_id <- decode_jwt(token)$payload$`custom:aplos_user_id`
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  complete <- FALSE
  while (!complete) {
    response <- GET(paste0(url,"/tenants/",tenant_id,"/users/",user_id,"/nca-engine/executions/",execution_id),
                    add_headers(.headers = headers))
    result <- fromJSON(content(response, "text", encoding = "UTF-8"))
    if(result$status == "failed") {break}
    complete <- result$status == "complete"
    if(!complete) {
      cat("Not yet complete ... ",result$status," \n")
      Sys.sleep(4)}
  }
  if(result$status == "complete") {
    cat("Execution complete. Execution ID = ",execution_id,"\n")
  } else {
    cat(paste0("Execution failed. Execution ID = ",execution_id,"\n"))
  }
  cat("Downloading results. \n")
  if(result$status == "complete") {
    download_url <- result$presigned$url
    output_file <- paste0(output,"results-",substr(execution_id,1,10),".zip")
    # create output directory if doesn't already exist
    download(download_url, dest=output_file, mode = "wb", quiet = TRUE)
    if(unzip) {
      unzip_folder = paste0(output,"results-",substr(execution_id,1,10))
      unzip(output_file, exdir = unzip_folder)
      cat("Results file downloaded and unziped. \n")
      cat(paste0("Location is ",unzip_folder,"/ \n"))
    } else {
      cat("Results file downloaded. \n")
    }
  }
```
