# Analysis Dataset Format
Analysis datasets are accepted in the following formats:
    -   comma separated variables (.csv)
    -   SAS Transport version 5 (.xpt)

## CSV
Comma separated variable format is the preferred format for files. These files are used in their native format without any conversion. 

## SAS XPT
SAS Transport files version 5 are accepted. These files are converted to CSV files prior to analysis. 

## Headers
The first row of the analysis dataset is assumed to contain column headers. Headers are imported "as-is" with no modifications. If two or more columns contain the same header (e.g. 2 columns named "subject"), then the left-most column will be used in the analysis.
