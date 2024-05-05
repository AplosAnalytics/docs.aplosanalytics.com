"""
Aplos Analytics
"""

class S3PresignedPayload:
    """ S3PresignedPayload """
    def __init__(self, payload: dict | None = None) -> None:
        self.bucket: str | None = None
        self.object_key: str | None = None
        self.url: str | None = None
        self.form_data: dict = {}        
        self.raw_payload: dict | None = payload
        if payload:
            self.__load(payload)

    def __load(self, payload: dict):

        if "presigned" not in payload:
            raise KeyError("Missing key 'presigned' in response payload.")
        self.url = payload["presigned"]["url"]
        self.form_data = self.__get_presigned_form_data(payload=payload)

        if "s3" not in payload:
            raise KeyError("Missing key 's3' in response payload.")

        self.bucket = payload["s3"]["bucket_name"]
        self.object_key = payload["s3"]["object_key"]

    def __get_presigned_form_data(self, payload: dict) -> dict:
        """
        Generates the form data need for an s3 presigned url upload
        NOTE: the order of the items below are important.  s3 presigned url uploads are
        very picky in the way the process the data.  if they are out of order you may get
        errors that the "keys" are not present.  It's best to centralize this into a library
        """
        form_data = {
            "key": payload["presigned"]["fields"]["key"],
            "x-amz-algorithm": payload["presigned"]["fields"]["x-amz-algorithm"],
            "x-amz-credential": payload["presigned"]["fields"]["x-amz-credential"],
            "x-amz-date": payload["presigned"]["fields"]["x-amz-date"],
            "x-amz-security-token": payload["presigned"]["fields"][
                "x-amz-security-token"
            ],
            "policy": payload["presigned"]["fields"]["policy"],
            "x-amz-signature": payload["presigned"]["fields"]["x-amz-signature"],
        }

        return form_data