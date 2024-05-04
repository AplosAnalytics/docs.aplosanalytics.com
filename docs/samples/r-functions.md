# 2️⃣ R Functions
The R functions used for interacting with Aplos NCA to analyze data are shown and described below. Code chunks look best in Dark mode. You can make the change at the top right of your browser.

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

## Acquire URL for file upload 
This function requests the secure URL to which you will upload the input data file. This function uses 3 pieces of information to acquire the upload URL. These are the input file name (`input_file`), URL for the API (`url`), and jwt (`token`). The URL for the API is available from the web interface under [Profile | API Configuration](./r-script.md#security-information).

```r:line-numbers
get_upload_url <- function(input_file,url,token){
  # url = api_url
  # token = current.jwt
  filename = str_split_i(input_file, "/", -1)
  upload_url = paste0(url,"/nca-engine/generate-upload-url")
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  body <- list(
    "file_name"=filename,
    method_type = "post"
  )
  
  response <- POST(url = upload_url,
                   add_headers(.headers = headers),
                   body = toJSON(body, auto_unbox = TRUE))
  
  result <- fromJSON(content(response, "text", encoding = "UTF-8"))
  return(result)
}
```

## Upload input data file 
This function uploads the data file for analysis using the secure URL. This function uses 2 pieces of information. These are the input file (`input_file`) and the response from the secure URL request (`result`). The response includes a security token that authenticates the user.

```r:line-numbers
upload_file_api <- function(input_file,result){
  upload_url = result$presigned$url
  headers <- c()
  body <- list(
    key = result$presigned$fields$key,
    "x-amz-algorithm" = result$presigned$fields$`x-amz-algorithm`,
    "x-amz-credential" = result$presigned$fields$`x-amz-credential`,
    "x-amz-date" = result$presigned$fields$`x-amz-date`,
    "x-amz-security-token" = result$presigned$fields$`x-amz-security-token`,
    policy = result$presigned$fields$policy,
    "x-amz-signature" = result$presigned$fields$`x-amz-signature`,
    file = upload_file(normalizePath(input_file))
  )
  
  response <- POST(url = upload_url, body = body)
}
```

## Initiate Analysis 
This function initiates the analysis by Aplos NCA. This function uses 5 pieces of information. These are the response from the secure URL request (result), the configuration settings (config.list), meta data (meta.list), jwt (token), and the URL for the API (url). The response from the secure URL request is used to identify the input analysis dataset location on the server for the anlaysis. The configuration settings and meta data must be list objects within R for this function to operate properly. The URL for the API is available from the web interface under [Profile | API Configuration](./r-script.md#security-information). 

```r:line-numbers
execute_analysis <- function(result,config.list,meta.list,token,url){
  # token = current.jwt
  # config.list = config.list
  # meta.list = meta.list
  # url = api_url
  # result = upload_result
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  body <- list(
    s3 = list(
      bucket_name = result$s3$bucket_name,
      object_key = result$s3$object_key
    ),
    meta_data = meta.list,
    configuration = config.list
  )
  
  response <- POST(url = paste0(url,"/nca-engine/executions"),
                   add_headers(.headers = headers),
                   body = toJSON(body, auto_unbox = TRUE))
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
This function checks the status of the analysis, prints that status, and then returns the download URL when the analysis is complete. This function uses 3 pieces of information. These are the URL for the API (`url`), jwt (`token`) and the unique analysis identifier (`execution_id`). The URL for the API is available from the web interface under [Profile | API Configuration](./r-script.md#security-information), and the unique analysis identifier is available from the response from the API when you initiate an analysis. 

```r:line-numbers
execution_status <- function(url,token,execution_id){
  # execution_id = exec_id
  # url = api_url
  # token = current.jwt
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  complete <- FALSE
  while (!complete) {
    response <- GET(paste0(url,"/nca-engine/executions/",execution_id),
                    add_headers(.headers = headers))
    result <- fromJSON(content(response, "text", encoding = "UTF-8"))
    if(result$status == "failed") {break}
    complete <- result$status == "complete"
    if(!complete) {
      cat(paste0("Not yet complete ... ",result$status," \n"))
      Sys.sleep(4)}
  }
  
  if(result$status == "complete") {
    cat("Execution complete. \n")
    cat(paste0("Execution duration = ",result$elapsed,". \n"))
    return(result)
  } else {
    cat(paste0("Execution failed. Execution ID = ",execution_id,"\n"))
  }
}
```
