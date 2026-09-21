
<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Presigned Upload Request
To upload a file into the Aplos NCA SaaS system, you will need to create a request for an AWS Presigned URL, which will allow you to upload the file.  You will use the response information to upload your file.

## Route

See [File System](../endpoints/routes#file-system) in the API routes reference (the upload-URL request).

## Payload

In the `payload` you will need to specify two fields.

|Name|Description|
|--|--|
|file_name|The name of the file.  Whatever you enter here will be name of the file stored in our system.  Typically you will name this the same as the actual file name, but you have an opportunity to override it here.|
|method_type|post|

```json
{
    
    "file_name": "<file-name>",
    "method_type": "post"
}

```

## Response

The response is wrapped in the standard success envelope. The `data` object
contains everything you need for the next steps.

> [!NOTE]
> You can send request fields in `camelCase` or `snake_case` — the API accepts
> either and normalizes to `snake_case` internally. Responses come back in
> `camelCase` to match the web app.

<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"         
    >
</CodeBlock>

## Fields needed for the File Upload Process
In the next section, we'll cover the process of uploading the file. You will
use the following fields from `data` during that process.

|Name|Description|
|--|--|
|url|The S3 endpoint to POST the file to.|
|fields|The S3 POST-policy form fields to include in the upload body (along with the file).|

## Fields needed when submitting an Analysis for an Execution
Later, when you [run an execution](./run_execution), you reference the uploaded
file by its `fileId` — returned as `data.fileId` in this response. Hold onto it.


## Example with 🐍 Python

This code sample wraps up the process of requesting the pre-signed URL and doing the upload.  

For this section, we'll focus on `def __get_presigned_upload_info(self, input_file: str) -> S3PresignedPayload:`, which generates the request.  

The result of the request is then handed off to another `python `module` which processes the resulting payload and creates a `form` upload object for uploading



<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/aws_s3_presigned_upload.py" 
    lang="python" 
    :displayLines="[{start:1, end: 20}, {start: 41, end: 78}]"
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/aws_s3_presigned_upload.py"
    >
</CodeBlock>