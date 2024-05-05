import os

import boto3
import requests

# Create a Cognito client



class CognitoUtility:
    def __init__(self, aws_region: str = "us-east-1"):
        self.id_token: str| None = None
        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.client = boto3.client("cognito-idp", region_name=aws_region)

    def login(self, username: str, password: str, client_id: str) ->str:
        return self.__authenticate(username, password, client_id)

    def __authenticate(self, username: str, password: str, client_id: str) -> str:
        """
        Get a JWT (JSON Web Token)
        """

        auth_response = self.client.initiate_auth(
            ClientId=client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": username, "PASSWORD": password},
        )

        if "ChallengeName" in auth_response:
            raise RuntimeError("New password required before a token can be provided.")

        # Extract the session tokens
        # id_token is the JWT token
        self.id_token = auth_response["AuthenticationResult"]["IdToken"]
        self.access_token = auth_response["AuthenticationResult"]["AccessToken"]
        self.refresh_token = auth_response["AuthenticationResult"]["RefreshToken"]

        return self.id_token


def get_required_environment_var(name: str):
    """
    Get an environment by name
    """
    value = os.getenv(name)
    if not value:
        message = f"missing required environment var {name}"
        print(message)
        raise RuntimeError(message)

    return value


def main():
    # Example usage to login to conginto with a username and password
    # The script below expects 3 environment varables to be set
    # create a local .env file and add the following with the appropriate values
    # COGNITO_CLIENT_ID=""
    # COGNITO_USER_NAME=""
    # COGNITO_PASSWORD=""

    aws_region = os.getenv("AWS_REGION", "us-east-1")
    client_id = get_required_environment_var("COGNITO_CLIENT_ID")
    uname = get_required_environment_var("COGNITO_USER_NAME")
    upassword = get_required_environment_var("COGNITO_PASSWORD")


    util = CognitoUtility(aws_region)
    
    jwt = util.login(uname, upassword, client_id)
    print("id token")
    print("###########################################################")
    print(jwt)
    print("###########################################################")

if __name__ == "__main__":
    main()
