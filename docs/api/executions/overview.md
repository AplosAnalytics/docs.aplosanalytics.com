# Analysis Exections Overview

The UI allows you to do the execution in 3 easy steps.
1. Upload your analysis file
Configure your inputs and optional metadata
3. Execute and wait for results.

For those 3 easy steps to occur there are additional things that the UI and its underlying framework do for you.
When you log in, your JWT is carried around with you like a security pass.
1. File uploads are securely uploaded with AWS S3 Presigned URLS.
2. Configurations are preloaded with a wizard / guided input.
3. After the execution submission, status checks are automatically polling.