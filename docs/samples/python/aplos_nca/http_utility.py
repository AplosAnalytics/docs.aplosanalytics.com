

class Urls:
    NCA_EXECUTIONS = "nca-engine/executions"
    NCA_GENERATE_UPLOAD = "nca-engine/generate-upload-url"


class HttpUtilities:

    @staticmethod
    def get_headers(jwt: str) -> dict:
        headers = {
            "Content-Type": "application/json",            
        }

        if jwt:
            headers["Authorization"] = f"Bearer {jwt}"

        return headers
    
    @staticmethod
    def get_route() ->str:
        return ""