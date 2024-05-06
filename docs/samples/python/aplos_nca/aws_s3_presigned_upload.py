"""
Aplos Analytics
"""

import json
import os
from urllib.parse import urljoin

import requests
from aws_s3_presigned_payload import S3PresignedPayload
from http_utility import HttpUtilities, Urls


class S3PresignedUpload:
    """S3PresignedUpload"""

    def __init__(self, jwt: str, api_url: str) -> None:
        self.api_url = api_url
        self.jwt = jwt

    def upload_file(self, input_file: str) -> S3PresignedPayload:
        """
        Uploads a file to your Aplos Cloud Account in AWS

        Args:
            input_file (str): path to the analysis file you are uploading

        Returns:
            S3PresignedPayload: an instance of S3PresignedPayload
        """

        # get the presigned url for uploading
        paylod: S3PresignedPayload = self.__get_presigned_upload_info(
            input_file=input_file
        )
        # upload the files
        self.__upload_file_to_s3(paylod, input_file=input_file)

        return paylod

    def __get_presigned_upload_info(self, input_file: str) -> S3PresignedPayload:
        """
        Performs all the necessary steps for creating a presigned url to upload a file to S3.
        We're using AWS S3 presigned urls for security as well as allowing for very large files if requried.
        Args:
            input_file (str): the path to the input (analysis) file

        Returns:
            S3PresignedPayload: instance of S3PresignedPayload
        """

        url = f"{self.api_url}/{Urls.NCA_GENERATE_UPLOAD}"
        headers = HttpUtilities.get_headers(self.jwt)

        body = {"file_name": input_file, "method_type": "post"}
        response = requests.post(
            url=url, headers=headers, data=json.dumps(body), timeout=30
        )

        if response.status_code == 403:
            raise PermissionError(
                "Failed to get a presigned url. "
                f"Status Code: {response.status_code }"
                f"Reason: {response.reason} "
                f"403 Errors can also occur if you have an invalid path."
            )
        elif response.status_code != 200:
            raise RuntimeError(
                "Failed to get a presigned url. "
                f"Status Code: {response.status_code }"
                f"Reason: {response.reason}"
            )
        result = response.json()

        payload: S3PresignedPayload = S3PresignedPayload(result)

        return payload

    def __upload_file_to_s3(self, payload: S3PresignedPayload, input_file: str) -> bool:
        """
        Peforms the actual uploading via a presigned url for S3 bucket storage
        Args:
            payload (S3PresignedPayload): instance of S3PresignedPayload with all the data needed
            input_file (str): the path to a file being uploaded

        Raises:
            FileNotFoundError: If the file is not found

        Returns:
            bool: True on success, False if not
        """

        if not os.path.exists(input_file):
            raise FileNotFoundError(
                "The input file you are submitting cannot be found.  Please check the path and try again."
            )

        with open(input_file, "rb") as file:
            files = {"file": (input_file, file)}
            # upload to s3 with the presigned url
            upload_response = requests.post(
                str(payload.url), data=payload.form_data, files=files, timeout=30
            )

        # Check the response: 204 is a success in this case
        if upload_response and upload_response.status_code == 204:
            print("\tFile uploaded successfully.")
            return True
        else:
            raise RuntimeError(
                "Error uploading the file. "
                f"Status Code: {upload_response.status_code}"
                f"Response: {upload_response.reason}"
            )
