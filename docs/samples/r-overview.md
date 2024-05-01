# Analysis with R

You can use R to perform analysis with Aplos NCA using API calls via secure http requests. Aplos has prepared sample scripts to illustrate how this analysis can be performed using R. One script includes functions for specific API requests and the second script includes code to execute a sample analysis and download the results. You can [download the files](/docs/downloads/r-files.zip) listed below to use as templates for executing an analysis with Aplos NCA using R.

| Description | File |
| :--- | :--- |
| API Functions | functions-api.R |
| Sample analysis | sample-analysis.R |
| Security file | security.txt |
| Sample data file | single_ev_10.csv |
| Configuration file | configuration_single_ev.json |
| Meta data file | meta_data.json |

## Functions

There are 5 functions provided to perform analysis with Aplos NCA. Detailed descriptions of the functions and the code are available on a separate [page](./r-functions.md). A short description can be found below:

| Function | Description |
| :--- | :---: |
| get_jwt | Request authentication JSON Web Token (jwt) from Amazon Cognito. This token is required for all API calls. |
| get_upload_url | Request Aplos NCA for secure URL to upload input data file. |
| upload_file_api | Securely upload input data file to user account. |
| execute_analysis | Initiate analysis. |
| execution_status | Request status of ongoing or completed analysis. |

## Example script

An example R script is provided that performs a complete analysis using Aplos NCA. The details of the example R script are available on a separate [page](./r-script.md). The R script performs the following actions:

1. Import security login information from a file
2. Request security token from Amazon Cognito
3. Request secure URL for input data file upload
4. Upload input data file
5. Initiate analysis with Aplos NCA
6. Check status of analysis and download results 
