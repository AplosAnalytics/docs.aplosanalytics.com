# ❗️ Required columns
The following columns are required for analysis with Aplos NCA:

 -   [Unique subject identifier](#unique-subject-identifier)
 -   [Time](#time)
 -   [Observed concentration](#observed-concentration)
 -   [Analyzed concentration](#analyzed-concentration)

## Unique subject identifier
The unique subject identifier column can contain alphanumeric information. Each unique value will be considered a unique subject in the analysis. The Unique subject identifier should be included as a Grouping column. In cases where there are multiple unique profiles for the same subject, grouping variables will be used to group data for those unique profiles. See [Optional Columns](./data-column-opt.md) for more information.

## Time
The time column must be in decimal format. It is recommended that this be the actual elapsed time since dose administration or nominal elapsed time since dose administration; however, nominal time can be used. Time (e.g. hh:mm) and Date/Time (dd mmm yyyy hh:mm) are not accepted for the time column. Time should be included as a Sorting column. 

## Observed concentration
This column can contain alphanumeric information and should include all observation information. This column can contain designations for samples that are below the limit of quantitation (e.g. BLQ, \<LLOQ, etc.), missing (e.g. NS, Missing, etc.). Currently, only designations for BLQ and missing samples are accepted.

## Analyzed concentration
This column must be in numeric format. Imputations for samples that are below the limit of quantitation or missing should be performed prior to upload in this column. For example, if all BLQ samples are imputed with 0, then a value of 0 should appear in the Analyzed concentration column for each BLQ sample. Aplos NCA does not perform any data manipulations prior to analysis.
