#!/bin/bash

# Amazon Cognito user pool details
# https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html
refresh_token="${REFRESH_TOKEN}"
client_id="${COGNITO_CLIENT_ID}"

# Amazon Cognito token endpoint

domain="cognito-idp.us-east-1.amazonaws.com/"
congito_url="https://${domain}"


payload="
{
    \"AuthParameters\" : {
       \"REFRESH_TOKEN\" : \"${refresh_token}\"
    },
    \"AuthFlow\" : \"REFRESH_TOKEN_AUTH\",
    \"ClientId\" : \"${client_id}\"
 }
"

# Make a POST request to the token endpoint to exchange refresh token for new access token
output=$(curl --request POST \
    --url ${congito_url} \
    --header 'X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth' \
    --header 'Content-Type: application/x-amz-json-1.1' \
    --data "${payload}")

# Extract the new access token from the response
#new_access_token=$(echo "$response" | jq -r '.access_token')

# Print the new access token
echo "New Access Token: $output"
