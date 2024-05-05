
<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
</script>

# Presigned Upload Request
To upload a file into the Aplos NCA SaaS system, you will need to create a request for an AWS Presigned URL, which will allow you to upload the file.  You will use the response information to upload your file.

## Route
<DisplayRoutes :route-id="['presigned_url']" :columns-to-show="['path', 'method_type']" />

## Payload

In the payload you will need to specify two fields.

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

```json
{
    "message": "File upload request created",
    "s3": {
        "bucket_name": "<s3-bucket-name>",
        "object_key": "<s3-object-key>"
    },
    "presigned": {
        "method_type": "post",
        "url": "<s3-bucket-url>",
        "fields": {
            "key": "<s3-object-key>",
            "x-amz-algorithm": "<x-amz-algorithm>",
            "x-amz-credential": "<x-amz-credential>",
            "x-amz-date": "<x-amz-date>",
            "x-amz-security-token": "<x-amz-security-token>",
            "policy": "<policy>",
            "x-amz-signature": "<x-amz-signature>"
        },
        "expires_in": 3600,
        "expires_at_utc": "<date-time-the-upload-url-will-expire>"
    },
    "file_name": "<file-name>"    
}
```

## Fields needed for the File Upload Process
In the next section, we'll cover the process of uploading a file.  You will need the following fields during that process.

```json
"url": "<s3-bucket-url>",
"fields": {
    "key": "<s3-object-key>",
    "x-amz-algorithm": "<x-amz-algorithm>",
    "x-amz-credential": "<x-amz-credential>",
    "x-amz-date": "<x-amz-date>",
    "x-amz-security-token": "<x-amz-security-token>",
    "policy": "<policy>",
    "x-amz-signature": "<x-amz-signature>"
},

```



## Fields needed when submitting an Analysis for an Execution
After you upload the file, and you submit an analysis for an execution you will need the following fields from the response.

```json
"s3": {
    "bucket_name": "<s3-bucket-name>",
    "object_key": "<s3-object-key>"
},

```