# Analysis Executions Overview
In this section, we'll cover the general flow of an analysis submission.


## Execution Flow
- Running NCA Calculations
- Combining Results across `profiles` (subjects and groups)
- Creating Plots
- Generating Reports

## The UI allows you to do the execution in 3 easy steps.
1. Upload your analysis file
2. Configure your inputs and optional metadata
3. Execute and wait for results.

## The Process
For those 3 easy steps to occur there are additional things that the UI does for you.

1. When you log in, your [JWT is returned from Cognito](./jwt) and "carried" around with you like a security pass.
1. File uploads
    - Presigned S3 File Upload [requests are created](./upload-request), returning a `fileId`
    - Files are [securely uploaded](./upload) with AWS S3 Presigned URLs
1. Configurations are preloaded with a wizard / guided input.
1. Executions are [submitted to the queue](./run_execution) with:
    - The uploaded file (`fileId`)
    - The configuration
    - Optional metadata
    - The response returns an `executionId`.
1. Using that `executionId`, [status checks](./status) are polled until the analysis is complete.

> [!TIP]
> In this section we outline the process of uploading a file and then doing the execution.  Just keep in mind that once a file is uploaded, you run multiple executions with different configurations against it.  
>
> Even better you can run them in parallel.  You don't need to wait for one to complete before launching another one.

> [!NOTE]
> Looking for the exact endpoints? See the [API routes reference](../endpoints/routes),
> organized by feature area.