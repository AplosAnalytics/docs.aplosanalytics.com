# 1️⃣ Analysis with R

You can use R to perform analysis with Aplos NCA using API calls via secure http requests. Aplos has prepared example R-scripts to illustrate how this analysis can be performed using R. One script includes functions for specific API requests and the second script includes code to execute a sample analysis and download the results. You can use the links below to see each file and the download it to your computer from the GitHub repository using the download link.   

| Description | File | Link to file |
| :--- | :--- | :---: |
| API Functions | functions-api.R | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/functions-api.R)|
| Sample analysis | sample-analysis.R | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/sample-analysis.R)|
| Security file | security.txt | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/security.txt)|
| Sample data file | single_ev.csv | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/single_ev.csv)|
| Configuration file | configuration_single_ev.json | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/configuration_single_ev.json)|
| Meta data file | meta_data.json | [:page_facing_up:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/blob/main/docs/downloads/r-files/meta_data.json)|
| Complete repository | all files | [:link:](https://github.com/AplosAnalytics/docs.aplosanalytics.com/tree/main/docs/downloads/r-files) |

## Functions

There is a single function that performs all actions needed to execute an analysis with Aplos NCA. A detailed description of the actions and the code are available on a separate [page](./r-functions.md). A short description can be found below:

| Function | Description |
| :--- | :--- |
| get_jwt | Request authentication JSON Web Token (jwt) from Amazon Cognito. This token is required for all API calls. |
| aplos_nca | Request Aplos NCA for secure URL to upload input data file. <br> Securely upload input data file to user account. <br> Initiate analysis. <br> Request status of ongoing or completed analysis. <br> Download and unzip the results to the local computer.|

## Sample analysis script

An example R script is provided that performs a complete analysis using Aplos NCA. The details of the example R script are available on a separate [page](./r-script.md). The R script performs the following actions:

1. Import security login information from a file
2. Request security token from Amazon Cognito
3. Execute analysis using Aplos NCA 
