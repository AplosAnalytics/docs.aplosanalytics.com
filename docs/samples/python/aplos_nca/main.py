import json
import os
import time
import zipfile
from datetime import datetime, timedelta
from pathlib import Path

import requests
from aws_cognito import CognitoAuthenication
from aws_s3_presigned_payload import S3PresignedPayload
from aws_s3_presigned_upload import S3PresignedUpload
from commandline_args import CommandlineArgs
from http_utility import HttpUtilities, Urls
from dotenv import load_dotenv

# load the environment (.env) file if any
load_dotenv()

class NCAEngine:
    """NCA Engine Access"""

    def __init__(
        self, api_url: str | None, cognito_client_id: str | None, region: str | None
    ) -> None:
        self.jwt: str
        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.api_url: str | None = api_url

        self.cognito: CognitoAuthenication = CognitoAuthenication(
            client_id=cognito_client_id, region=region
        )

        if not self.api_url:
            raise RuntimeError(
                "Missing Aplos Api Url. "
                "Pass in the api_url as a command arg or set the APLOS_API_URL environment var."
            )

    def execute(
        self,
        username: str,
        password: str,
        input_file_path: str,
        config_data: dict,
        *,
        meta_data: str | dict | None = None,
        wait_for_results: bool = True,
        output_directory: str | None = None,
        unzip_after_download: bool = False,
    ) -> None:
        """_summary_

        Args:
            username (str): the username
            password (str): the users password
            input_file_path (str): the path to the input (anlysis) file
            config_data (dict): analysis configuration infomration
            meta_data (str | dict | None, optional): meta data attached to the execution. Defaults to None.
            wait_for_results (bool, optional): should the program wait for results. Defaults to True.
            output_directory (str, optional): the output directory. Defaults to None (the local directy is used)
            unzip_after_download (bool): Results are downloaded as a zip file, this option will unzip them automatically.  Defaults to False
        """

        print("\tLogging in.")
        self.jwt = self.cognito.login(username=username, password=password)

        print("\tUploading the analysis file.")
        uploader: S3PresignedUpload = S3PresignedUpload(self.jwt, str(self.api_url))
        presign_payload: S3PresignedPayload = uploader.upload_file(input_file_path)

        print("\tStarting the execution.")
        execution_id = self.run_analysis(
            bucket_name=str(presign_payload.bucket),
            object_key=str(presign_payload.object_key),
            config_data=config_data,
            meta_data=meta_data,
        )

        if execution_id and wait_for_results:
            # wait for it
            download_url = self.wait_for_results(execution_id=execution_id)
            # download the files
            if download_url:
                print("\tDownloading the results.")
                self.download_file(
                    download_url,
                    output_directory=output_directory,
                    do_unzip=unzip_after_download,
                )

    def run_analysis(
        self,
        bucket_name: str,
        object_key: str,
        config_data: dict,
        meta_data: str | dict | None = None,
    ) -> str:
        """
        Run the analysis

        Args:
            bucket_name (str): s3 bucket name for your organization. this is returned to you
            object_key (str): 3s object key for the file you are running an analysis on.
            config_data (dict): the config_data for the analysis file
            meta_data (str | dict): Optional.  Any meta data you'd like attached to this execution
        Returns:
            str: the execution id
        """

        headers = HttpUtilities.get_headers(self.jwt)
        # to start a new execution we need the location of the file (s3 bucket and object key)
        # you basic configuration
        # optional meta data

        submission = {
            "s3": {"bucket_name": bucket_name, "object_key": object_key},
            "configuration": config_data,
            "meta_data": meta_data,
        }
        url = f"{str(self.api_url)}/{Urls.NCA_EXECUTIONS}"
        response: requests.Response = requests.post(
            url, headers=headers, data=json.dumps(submission), timeout=30
        )
        json_response: dict = response.json()

        if response.status_code == 403:
            raise PermissionError(
                "Failed to execute.  A 403 response occured.  "
                "This could a token issue or a url path issue  "
                "By default unknown gateway calls return 403 errors. "
            )
        elif response.status_code != 200:
            raise RuntimeError(
                f"Unknown Error occured during executions: {response.status_code}. "
                f"Reason: {response.reason}"
            )

        execution_id = str(json_response.get("execution_id"))
        print(f"\tExecution {execution_id} started.")

        return execution_id

    def wait_for_results(
        self, execution_id: str, max_wait_in_minutes: int = 5
    ) -> str | None:
        """
        Wait for results
        Args:
            execution_id (str): the analysis execution id

        Returns:
            str | None: on success: a url for download, on failure: None
        """

        url = f"{self.api_url}/{Urls.NCA_EXECUTIONS}/{execution_id}"

        headers = HttpUtilities.get_headers(self.jwt)
        current_time = datetime.now()
        # Create a timedelta object representing 15 minutes
        time_delta = timedelta(minutes=max_wait_in_minutes)

        # Add the timedelta to the current time
        max_time = current_time + time_delta

        complete = False
        while not complete:
            response = requests.get(url, headers=headers, timeout=30)
            json_response: dict = response.json()
            status = json_response.get("status")
            complete = status == "complete"
            elapsed = json_response.get("elapsed")
            if status == "failed" or complete:
                break
            if not complete:
                print(f"\t\twaiting for results.... {status}: {elapsed}")
                time.sleep(5)
            if datetime.now() > max_time:
                status = "timeout"
                break
            if status is None and elapsed is None:
                # we have a problem
                status = "unknown issue"
                break

        if status == "complete":
            print("\tExecution complete.")
            print(f"\tExecution duration = {elapsed}.")
            return json_response["presigned"]["url"]
        else:
            print(
                f"\tExecution failed. Execution ID = {execution_id}. reason: {json_response.get('errors')}"
            )
            return None

    def download_file(
        self,
        presigned_download_url: str,
        output_directory: str | None = None,
        folder: str | None = None,
        do_unzip: bool = False,
    ) -> str | None:
        """
        # Step 5
        Download completed analysis files

        Args:
            presigned_download_url (str): presigned download url
            output_directory (str | None): optional output directory

        Returns:
            str: file path to results or None
        """
        if output_directory is None:
            output_directory = str(Path(__file__).parent)
            output_directory = os.path.join(output_directory, ".output")
        else:
            folder = output_directory
            output_directory = str(Path(__file__).parent)
            output_directory = os.path.join(output_directory, folder)

        if presigned_download_url:
            output_file = f"results-{time.strftime('%Y-%m-%d-%Hh%Mm%Ss')}.zip"

            output_file = os.path.join(output_directory, output_file)
            os.makedirs(output_directory, exist_ok=True)

            response = requests.get(presigned_download_url, timeout=60)
            # write the zip to a file
            with open(output_file, "wb") as f:
                f.write(response.content)

            # optionally, extract all the files from the zip
            if do_unzip:
                with zipfile.ZipFile(output_file, "r") as zip_ref:
                    zip_ref.extractall(output_file.replace(".zip", ""))

            unzipped_state = "and unzipped" if do_unzip else "in zip format"

            print(f"\tResults file downloaded {unzipped_state}.")
            print(f"\t\tResults are available in: {output_directory}")

            return output_directory
        else:
            return None


def main():
    try:
        print("Welcome to the NCA Engine Upload & Execution Demo")
        args = CommandlineArgs()
        files_path = os.path.join(Path(__file__).parent, "files")

        args.analysis_file_default = os.path.join(files_path, "single_ev.csv")
        args.config_file_default = os.path.join(
            files_path, "configuration_single_ev.json"
        )
        args.metadata_file_default = os.path.join(files_path, "meta_data.json")
        if not args.is_valid():
            print("\n\n")
            print("Missing some arguments.")
            exit()

        
        engine = NCAEngine(
            api_url=args.api_url,
            cognito_client_id=args.cognito_client_id,
            region=args.aws_region,
        )

        print("\tLoading analysis configurations")
        print(f"\t\t{args.config_file}")
        config_data: dict = read_json_file(str(args.config_file))

        print("\tLoading analysis meta data")
        print(f"\t\t{args.metadata_file}")
        meta_data = optional_json_loads(read_text_file(str(args.metadata_file)))

        engine.execute(
            username=str(args.username),
            password=str(args.password),
            input_file_path=str(args.analysis_file),
            config_data=config_data,
            meta_data=meta_data,
            output_directory=str(args.output_directory),
        )
        print("Thank you for using the NCA Engine Upload and Execution Demo")
    except Exception as e:  # pylint: disable=w0718
        print("An error occured ... exiting with an error")
        print(str(e))


def optional_json_loads(data: str | dict) -> str | dict:
    """
    Attempts to load the data as json, fails gracefull and retuns the data is if it fails
    Args:
        data (str): data as string

    Returns:
        str | dict: either the data as is or a converted dictionary/json object
    """
    if isinstance(data, dict):
        return data

    try:
        data = json.loads(str(data))
    finally:
        pass
    return data


def read_json_file(file_path: str) -> dict:
    """
    Reads a file and returns the json
    Args:
        file_path (str): _description_

    Raises:
        FileNotFoundError: _description_

    Returns:
        dict: _description_
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File Not Found: {file_path}")

    data = None
    with open(file_path, mode="r", encoding="utf8") as file:
        data = json.load(file)

    return data


def read_text_file(file_path: str) -> str:
    """
    Read files contents
    Args:
        file_path (str): path to the file

    Raises:
        FileNotFoundError: if the file is not found

    Returns:
        str: the files data
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File Not Found: {file_path}")

    data = None
    with open(file_path, mode="r", encoding="utf8") as file:
        data = file.read()

    return data


if __name__ == "__main__":
    main()
