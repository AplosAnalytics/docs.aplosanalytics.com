#!/bin/bash

## 🚨 IMPORTANT USE THIS DOMAIN 🚨
## you may need to change the region but that's it 
## don't use the custom domain or the script will fail with 302 error
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

echo "payload below - usefull for troubleshooting"
echo $payload

echo ""
echo "response:"
echo ""

curl --request POST \
    --url ${congito_url} \
    --header 'X-Amz-Target: AWSCognitoIdentityProviderService.InitiateAuth' \
    --header 'Content-Type: application/x-amz-json-1.1' \
    --data "${payload}"

