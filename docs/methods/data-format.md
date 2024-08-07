# 📚 Analysis Dataset Format
Analysis datasets are accepted in the following formats:

-   [comma separated variables (.csv)](#csv)
-   [SAS Transport version 5/8 (.xpt)](#sas-transport-xpt)
-   [SAS Dataset file version 7-9 (.sas7bdat)](#sas-dataset)
-   [text delimited files (.dat)](#text-delimited)

## CSV
Comma separated variable format is the preferred format for files. These files are used in their native format without any conversion. 

## SAS Transport (XPT)
SAS&copy; Transport files (versions 5 and 8) are accepted. These files are converted to CSV format prior to analysis. When you download the results you will receive the original formatted file and the converted CSV file for review.

## SAS Dataset
SAS&copy; Transport files (version 7 through 9) are accepted. These files are converted to CSV format prior to analysis. When you download the results you will receive the original formatted file and the converted CSV file for review.

## Text Delimited
Text delimited files are also accepted using standard delimiters like pipe (|), colon (\:), space, and tab. These files are converted to CSV format prior to analysis. When you download the results you will receive the original formatted file and the converted CSV file for review.

## Headers
The first row of the analysis dataset is assumed to contain column headers. Headers are imported "as-is" with no modifications. Here are some recommendations:

 -  Use unique column headers for each column of data. 
 -  Do not use special characters (e.g. `*&^%$#@!)(|\/`) in your headers.
 -  Headers are case sensitive. It is recommended to use either all capital letters or all lowercase headers in your headers.

> [!WARNING]
>  -    Do not include more than one header row. Datasets with more than one header row will give errors in the analysis. The second header row will be treated like data and is likely to cause an error.
>  -    Do not duplicate column headers in the dataset. Only the first instance of a column name will be recognized.
>  -    Do not include units in your headers as the special characters (e.g. `(ng/ml)` or `(m^2)`) will cause errors in the analysis.

