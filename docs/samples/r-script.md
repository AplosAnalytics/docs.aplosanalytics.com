# R Example Script

The example R script performs a complete analysis with Aplos NCA from R. 

## Example Script

The following line numbers include key information that must be updated in the script on the user's system. Those line numbers are also highlighted in the code below.

-   Line 11: include the name and location of the file with the security information. Including security login information directly in a script (e.g. Lines 12-16) is not recommended. The structure of the [security file](#security-information) can be found below the example R script.
-   Line 20: include the name and location of the file with the input data
-   Line 21: include the name and location of the configuration json file
-   Line 22: include the name and location of the meta data json file
-   Line 60: include the name and location of the output folder for the results

```r:line-numbers {11,20,21,22,60}
# Clear all objects
rm(list = ls())

# change to TRUE to unzip the output file
unzip = FALSE 

# import functions needed to run API
source("functions-api.R")

# Grab login variables from security file
source("security.txt")
username = COGNITO_USER_NAME
password = COGNITO_PASSWORD
client_id = COGNITO_CLIENT_ID
region = COGNITO_REGION
api_url = APLOS_API_URL

# here are some default file and config setups
# adjust your code accordingly
input_file = "../single_ev_10.csv"
config_file = "./files/configuration_single_ev.json"
meta_file = "./files/meta_data.json"

# Record the start time for the script
start_time <- Sys.time()

cat("Welcome to the NCA Engine Upload & Execution Demo \n")

# Log into Amazon cognito to get authorization token
cat("Log in ... \n")
current.jwt <- get_jwt(client_id,username,password,region)

# Request secure URL for uploading input file then upload the data input file
cat("Uploading input file ... \n")
upload_result <- get_upload_url(input_file = input_file, url = api_url, token = current.jwt)
upload_file_api(input_file = input_file, result = upload_result)

# Import analysis configuration file
cat("Loading analysis configurations \n")
config.list <- fromJSON(txt = config_file)

# Import meta data file
cat("Loading analysis meta data \n")
meta.list <- fromJSON(txt = meta_file)

# Initiate analysis 
cat("Initiating analysis ... \n")
exec_id <- execute_analysis(result = upload_result, config.list = config.list,
                            meta.list = meta.list, url = api_url, token = current.jwt)

# Check status of analysis. If not complete, this continues checking until it is complete or failed
cat("Checking status \n")
exec_result <- execution_status(url = api_url, token = current.jwt, execution_id = exec_id)

# If analysis is complete, download completed analysis files
if(exec_result$status == "complete") {
  download_url <- exec_result$presigned$url
  output_file <- paste0(".output/output-",format(Sys.time(),"%Y-%m-%d-%Hh%Mm%Ss"),".zip")
  # create output directory if doesn't already exist
  if (!dir.exists(".output")) {dir.create(".output")}
  download(download_url, dest=output_file, mode = "wb", quiet = TRUE)
  if(unzip) {
    unzip(output_file, exdir = ".output/unzip")
    cat("Results file downloaded and unziped. \n")
    cat(paste0("Location is .output/unzip \n"))
  } else {
    cat("Results file downloaded. \n")
  }
  
}

end_time <- Sys.time()
total_time <- hms_span(start_time,end_time)
cat(paste0("Total runtime was ",total_time," (Hours:Minutes:Seconds) \n"))

```

## Security Information

Security information should never be stored within a script that is shared with other users. One method to simplify use of security information within R is to create a text file with the security information that is then imported into the script and used. Let others know that they will need to use their own security information file when using the code. The security.txt file in the [r-files.zip](https://44996058.fs1.hubspotusercontent-na1.net/hubfs/44996058/public/r-files.zip) package shows the format, but contains no information.

The information for everything except the username and password can be obtained from the Aplos NCA Web Interface under the [Profile | API Configuration](./r-script.md#security-information). 
![API Configuration](./images/API%20Configuration%20blur.png)

Enter the information from your account inside the quotation marks and then save the file on your computer to be imported into the Example R script. 

```r:line-numbers
APLOS_API_URL="<value here>"
COGNITO_CLIENT_ID="<value here>"
COGNITO_USER_NAME="<value here>"
COGNITO_PASSWORD="<value here>"
COGNITO_REGION="<value here>"
```