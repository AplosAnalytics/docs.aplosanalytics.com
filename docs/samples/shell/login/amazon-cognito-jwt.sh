#!/bin/bash

# file name: amazon-cognito-jwt.sh

# AWS DOCS for using Cognito JWT
# https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html

## 🚨 IMPORTANT USE THIS DOMAIN 🚨
## "cognito-idp.<aws-region>.amazonaws.com/"
## you may need to change the region but that's it 
## don't use the custom domain or the script will fail with 302 error
## for example, some documentation says to use
## https://<your-id-or-domain>.auth.<your-region>.amazoncognito.com/oauth2/token
## but don't, it will lead you down a rabbit hole of 302 errors
## 👇👇👇👇👇👇👇
domain="cognito-idp.us-east-1.amazonaws.com/"
congito_url="https://${domain}"


username="${COGNITO_USER_NAME}"
password="${COGNITO_PASSWORD}"
client_id="${COGNITO_CLIENT_ID}"


# AuthFlow: USER_PASSWORD_AUTH
# requires ALLOW_USER_PASSWORD_AUTH in the configured Cognito Authentication Flows
payload="
{
    \"AuthParameters\" : {
       \"USERNAME\" : \"${username}\",
       \"PASSWORD\" : \"${password}\"
    },
    \"AuthFlow\" : \"USER_PASSWORD_AUTH\",
    \"ClientId\" : \"${client_id}\"
 }
"

echo "\n"
echo "\n"

echo "payload below - usefull for troubleshooting"
echo $payload

echo "\n"
echo "\n"

output=$(curl --request POST \
    --url ${congito_url} \
    --header 'X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth' \
    --header 'Content-Type: application/x-amz-json-1.1' \
    --data "${payload}")


echo $output
