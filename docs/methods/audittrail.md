# Audit Trail
All API actions are logged by Aplos NCA within the user/team account. 

## Unique User Identifier
Each user account has a unique identification code for that user. All actions performed by that user are logged with the unique identification code. In Team accounts, administrators can search for all activity by a specific user (or set of users) by searching using the unique identification code.

## Logging
Aplos NCA logs all API calls in the database. This includes all analysis dataset uploads, all analysis execution requests, and all analysis status requests and downloads. 

## Modifications
Aplos NCA does not allow modifications to any files. If corrections need to be made to an analysis dataset, the user must upload a new dataset, which will receive a separate unique file identifier. If corrections are needed to the configuration for an analysis, a new analysis must be executed and new results with a new unique execution identifier will be created.

For every execution, there will be a single analysis dataset and a single set of results. An analysis dataset can be used for multiple executions; however, results will only be associated with a single analysis dataset and configuration file. 

## Deletions
Aplos NCA does allow deletion of both analysis datasets and analysis results; however, the deletion is logged in the database. The unique file identifier is retained, and the date, time, and user that requested deletion is noted. Similarly, if analysis results are deleted, the unique execution identifier is retained and the date, time, and user that requested deletion is noted. Aplos Analytics does not recommend using the deletion function, except in rare cases. There is no method to restore deleted files.
