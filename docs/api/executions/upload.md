<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
import CodeBlock from '/docs/components/CodeBlock.vue'
</script>

# Upload your analysis file

Now that you have a pre-signed URL to upload your file, it's time to do the actual upload.

You'll use information from the pre-signed generation to do the upload.

## Route
<DisplayRoutes :route-id="['file_upload']" :columns-to-show="['path', 'method_type']" />

## The Response from the Upload Request

In the previous step, you initiated a pre-signed url request.   The response from that will request will contain the `"presigned":"url"`, which will become the url enpoint for the POST upload action to upload a file.

Below is the basic structure of the response created from the pre-signed url request.
<CodeBlock 
    link="https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/api/executions/upload-request-response.json"
    src="https://raw.githubusercontent.com/AplosAnalytics/docs.aplosanalytics.com/main/docs/api/executions/upload-request-response.json" 
    lang="json"
    :highlightLines=[9]        
    >
</CodeBlock>

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


## The Response of an Upload -> 204 Ok ~ No Content

The response from uploading a file with a pre-signed URL is simply `204` with no body or other information.  It's essentially a response that the information was received and it will be available shortly. S3 works on an eventual consistency model as it replicates this across several availability zones.

Typically your file is ready almost immediately.  And, since our executions are queued, you can request the start an execution right away.
