
<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Presigned Upload Request
To upload a file into the Aplos NCA SaaS system, you will need to create a request for an AWS Presigned URL, which will allow you to upload the file.  You will use the response information to upload your file.

## Route
<DisplayRoutes :route-id="['presigned_url']" :columns-to-show="['path', 'method_type']" />

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

The response will contain a decent amount of information that you will need to carry along for the next steps.

<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"         
    >
</CodeBlock>



## Fields needed for the File Upload Process
In the next section, we'll cover the process of uploading a file.  You will need the following fields during that process.

|Name|Description|
|--|--|
|url|The endpoint for the file upload|
|fields|All the necessary fields you'll need to submit in the body of the payload (along with the file)|


<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"
    :displayLines="[1, {start:9, end: 18}, 23]"        
    >
</CodeBlock>


## Fields needed when submitting an Analysis for an Execution
Later after the file is uploaded, you will want to run an execution. Part of the payload to start an execution is the file location in S3.  You will need the `bucket name` and `object key` which can be found in this payload.


<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"
    :displayLines="[{start:1, end: 6}, 23]"        
    >
</CodeBlock>


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