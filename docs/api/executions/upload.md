<script setup>
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Upload your analysis file

Now that you have a pre-signed URL to upload your file, it's time to do the actual upload.

You'll use information from the pre-signed generation to do the upload.

## Route

The upload is a direct `POST` to the presigned S3 URL returned by the
[upload-URL request](./upload-request) — it is not a route on the Aplos API.

## Payload


## Response

In the previous step, you requested a presigned upload. That response contains
`data.url` (the S3 endpoint) and `data.fields` (the S3 POST-policy form fields).
You POST the file to `data.url` with those `data.fields` included in the form body.

Below is the basic structure of that presigned upload response.
<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"
    >
</CodeBlock>



> [!NOTE] The Response of an Upload -> 204 ~ No Content (not 200)
>
>The response from uploading a file with a pre-signed URL is simply `204` with no body or other information.  It's essentially a response that the information was received and it will be available shortly. S3 works on an eventual consistency model as it replicates this across several availability zones.
>
>**Keep that in mind if you are only used to checking for 200 responses.**
>
>Typically your file is ready almost immediately.  And, since our executions are queued, you can request the start an execution right away.

## Example with 🐍 Python

This code block contains the full source, which also includes the initial request to get the pre-signed url (from the previous section).
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/aws_s3_presigned_upload.py" 
    lang="python"
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/aws_s3_presigned_upload.py"    
    >
</CodeBlock>

## Generating the Payload

The Code Block above calls this class to create the Payload for the upload.
<CodeBlock 
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/samples/python/aplos_nca/aws_s3_presigned_payload.py" 
    lang="python"
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/samples/python/aplos_nca/aws_s3_presigned_payload.py"
    >
</CodeBlock>



