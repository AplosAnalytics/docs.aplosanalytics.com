import os

class EnvironmentVars:
    def __init__(self) -> None:
        self.api_url = os.getenv("APLOS_API_URL")
        self.aws_region = os.getenv("AWS_REGION") or os.getenv("COGNITO_REGION")
        self.client_id = os.getenv("COGNITO_CLIENT_ID")
        self.username = os.getenv("COGNITO_USER_NAME")
        self.password = os.getenv("COGNITO_PASSWORD")

        self.config_file = os.getenv("CONFIG_FILE")
        self.metadata_file = os.getenv("METADATA_FILE")
        self.analysis_file = os.getenv("ANALYSIS_FILE")