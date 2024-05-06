import os
import boto3


class CognitoAuthenication:
    def __init__(self, client_id: str | None, region: str | None) -> None:
        # setup the client id
        self.client_id: str | None = client_id
        self.jwt: str
        self.access_token: str
        self.refresh_token: str
        self.region: str = region or "us-east-1"
        self.client = boto3.client("cognito-idp", region_name=region)

        if self.client_id is None:
            raise RuntimeError(
                "Missing Cognito Client Id. "
                "Pass in a client_id as a command arg or set the COGNITO_CLIENT_ID enviornment var"
            )

    def login(self, username: str, password: str) -> str:
        """
        Get a JWT (JSON Web Token)

        Args:
            username (str): username (email address)
            password (str): password
            client_id (str): cognito client/application id

        Returns:
            str | None: json web token (jwt)
        """

        auth_response = self.client.initiate_auth(
            ClientId=self.client_id,
            # user USER_PASSWORD_AUTH flow for this type of login
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={"USERNAME": username, "PASSWORD": password},
        )

        if "ChallengeName" in auth_response:
            # depending on your setup, it's possible you will get challenged for a
            # password change. contact support if this happens
            raise RuntimeError(
                "New password required before a token can be provided. Please contact support or your Aplos Administrator."
            )

        # Extract the session tokens
        # id_token is the JWT token
        # typical tokens last for 30 minutes to 1 hour by default
        self.jwt = auth_response["AuthenticationResult"]["IdToken"]
        # access token is if you have direct access to aws resources
        # you probably won't ever need this
        self.access_token = auth_response["AuthenticationResult"]["AccessToken"]  # noqa: F814, F841, pylint: disable=W0612
        # refresh token if needed
        # you can use refresh tokens to "refresh" your jwt or simply login again
        # refresh tokens are typically good for 30 days by default
        self.refresh_token = auth_response["AuthenticationResult"]["RefreshToken"]  # noqa: F814, F841, pylint: disable=w0612

        # return the jwt token
        return self.jwt
