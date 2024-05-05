<script setup>
import DisplayRoutes from '/docs/components/DisplayRoutes.vue'
</script>

# Upload your analysis file

Now that you have a pre-signed URL to upload your file, it's time to do the actual upload.

You'll use information from the pre-signed generation to do the upload.

## Route
<DisplayRoutes :route-id="['file_upload']" :columns-to-show="['path', 'method_type']" />

## Upload Request Response

In the previous step, you initiated a pre-signed url request, in the response you will need to get the "presigned":"url", which will become the url for the POST upload action to upload a file.

```json:line-numbers {7,9}
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

