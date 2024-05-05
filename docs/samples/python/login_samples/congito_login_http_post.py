import json
import os

import requests


def login(
    username: str, password: str, client_id: str, region: str = "us-east-1"
) -> tuple[str, str, str]:
    congito_url = f"https://cognito-idp.{region}.amazonaws.com/"

    headers = {
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
        "Content-Type": "application/x-amz-json-1.1",
    }

    body = {
        "AuthParameters": {"USERNAME": username, "PASSWORD": password},
        "AuthFlow": "USER_PASSWORD_AUTH",
        "ClientId": client_id,
    }

    body = json.dumps(body)

    response = requests.post(url=congito_url, data=body, headers=headers, timeout=10)
    result = json.loads(response.content)
    # IdToken is the JWT you will need
    id_token = result["AuthenticationResult"]["IdToken"]
    access_token = result["AuthenticationResult"]["AccessToken"]
    refresh_token = result["AuthenticationResult"]["RefreshToken"]

    # return all three in case we need them
    return id_token, access_token, refresh_token



def main():
    # example usage
    client_id = os.getenv("COGNITO_CLIENT_ID", "")
    username = os.getenv("COGNITO_USER_NAME", "")
    password = os.getenv("COGNITO_PASSWORD", "")

    token = login(username, password, client_id)
    jwt = token[0]
    print(jwt)

if __name__ == "__main__":
    main()
    
