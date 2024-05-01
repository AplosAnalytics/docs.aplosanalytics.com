# R Functions for Aplos API
suppressPackageStartupMessages(library(httr))
suppressPackageStartupMessages(library(jsonlite))
suppressPackageStartupMessages(library(downloader))
suppressPackageStartupMessages(library(stringr))

hms_span <- function(start, end) {
  dsec <- as.numeric(difftime(end, start, unit = "secs"))
  hours <- floor(dsec / 3600)
  minutes <- floor((dsec - 3600 * hours) / 60)
  seconds <- dsec - 3600*hours - 60*minutes
  paste0(
    sapply(c(hours, minutes, seconds), function(x) {
      formatC(x, width = 2, format = "d", flag = "0")
    }), collapse = ":")
}

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
