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

aplos_nca <- function(token = jwt, input, config, meta, url, output = "./", unzip = TRUE){
  cat("Welcome to the NCA Engine Upload & Execution Script\n")
  # Get pre-signed URL
  filename = str_split_i(input, "/", -1)
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
  upload_url_result <- fromJSON(content(response, "text", encoding = "UTF-8"))
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
  cat("Loading analysis configurations \n")
  config.list <- fromJSON(txt = config)
  
  cat("Loading analysis meta data \n")
  meta.list <- fromJSON(txt = meta)
  
  cat("Initiating analysis ... \n")
  headers <- c("Content-Type" = "application/json",
               "Authorization" = paste0("Bearer ",token))
  body <- list(
    file = list(
      id = upload_url_result$file$id
    ),
    meta_data = meta.list,
    configuration = config.list
  )
  
  analysis_response <- POST(url = paste0(url,"/nca-engine/executions"),
                            add_headers(.headers = headers),
                            body = toJSON(body, auto_unbox = TRUE))
  if (http_status(analysis_response)$category == "Success") {
    cat("Execution initiated. \n")
  } else {
    cat("Error in the request. \n")
  }
  analysis_response2 <- fromJSON(content(analysis_response, "text", encoding = "UTF-8"))
  execution_id <- analysis_response2$execution_id
  
  cat("Checking status ... \n")
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
}