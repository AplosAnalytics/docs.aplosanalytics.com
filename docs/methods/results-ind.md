# Individual PK Parameters
The results include the individual PK parameters for each unique profile included in the analysis. The results are presented in 3 separate files as described below.

## File: pk-listing.csv and pk-listing.html
These files include the individual PK parameters for each unique profile in the analysis. The CSV and HTML files include the same information with the same column structure. The individual PK parameters presented include those that can be calculated without the terminal elimination rate constant and those that require the terminal elimination rate constant derived from the best-fit Kel rules. All subjects and all profiles are included in each of these files.

## File: pk-results.csv
This file includes the individual PK parameters for each unique profile and for each estimated terminal elimination rate constant group. As described in the [Terminal Slope method](./terminalslope), Aplos NCA calculates mutliple terminal slope values for each profile, and all parameters associated with that terminal slope. Therefore, a single individual may have 9 terminal slope estimates for the same profile. Results for all 9 terminal slope estimates are included in the pk-results.csv file. The column named group can be used to identify the parameters associated with each terminal slope estimate. Group 0 refers to the PK parameters that can be calculated without the terminal slope.

## Folder: Individuals
Within this folder, a separate CSV file is produced from the pk-results.csv file by extracting all parameters for a single subject profile. These individual files contain the same information as the pk-results.csv file; however, it may be easier to view this information divided by single subjects.
