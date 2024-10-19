class Urls:
    NCA_EXECUTIONS = "nca/executions"
    NCA_GENERATE_UPLOAD = "nca/files"


class HttpUtilities:
    """Http Utilties"""

    @staticmethod
    def get_headers(jwt: str) -> dict:
        """Get the Http Headers"""
        headers = {
            "Content-Type": "application/json",
        }

        if jwt:
            headers["Authorization"] = f"Bearer {jwt}"

        return headers
