# Analysis Executions Overview

Analysis Executions refers to the process of:
- Running NCA Calculations
- Combining Results across `profiles` (subjects and groups)
- Creating Plots
- Generating Reports

The UI allows you to do the execution in 3 easy steps.
1. Upload your analysis file
2. Configure your inputs and optional metadata
3. Execute and wait for results.

For those 3 easy steps to occur there are additional things that the UI does for you.

1. When you log in, your [JWT is returned from Cognito](./jwt) and "carried" around with you like a security pass.
1. File uploads
    - Presigned S3 File Upload [requests are created](./upload-request.md)
    - Files are [securely uploaded](./upload.md) with AWS S3 Presigned URLS
1. Configurations are preloaded with a wizard / guided input.
1. Executions are [requested](./run.md) with:
    - The analysis file information
    - The configuration
    - Optional Meta Data
1. After the execution submission, [status checks](./status.md) are automatically polled and displayed in the UI.