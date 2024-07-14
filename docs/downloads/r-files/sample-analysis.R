# Clear all objects
rm(list = ls())

# import functions needed to run API
source("functions-api.R")

# Grab login variables from file (see readme for details)
source(".env")
username = COGNITO_USER_NAME
password = COGNITO_PASSWORD
client_id = COGNITO_CLIENT_ID
region = COGNITO_REGION
api_url = APLOS_API_URL

# here are some default file and config setups.
# adjust your code accordingly
input_file = "./files/single_ev.csv"
config_file = "./files/configuration_single_ev.json"
meta_file = "./files/meta_data.json"

# Record the start time for the script
start_time <- Sys.time()

cat("Log in ... \n")
jwt <- get_jwt(client_id,username,password,region)

aplos_nca(token = jwt,
          input = input_file,
          config = config_file,
          meta = meta_file,
          url = api_url,
          output = "./",
          unzip = TRUE)

# Record the end time for the script
end_time <- Sys.time()
total_time <- hms_span(start_time,end_time)
cat(paste0("Total runtime was ",total_time," (Hours:Minutes:Seconds) \n"))
