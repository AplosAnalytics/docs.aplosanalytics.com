# Required columns
The following columns are required for analysis with Aplos NCA:

 -   [Unique subject identifier](#unique-subject-identifier)
 -   [Time](#time)
 -   [Observed concentration](#observed-concentration)
 -   [Analyzed concentration](#analyzed-concentration)

## Unique subject identifier
The unique subject identifier column can contain alphanumeric information. Each unique value will be considered a unique subject in the analysis. In cases where there are multiple unique profiles for the same subject, sorting variables will be used to group data for those unique profiles. See [Optional Columns](./data-column-opt.md) for more information.

## Time
The time column must be in decimal format. It is recommended that this be the actual elapsed time since dose administration or nominal elapsed time since dose administration. 

## Observed concentration
This column can contain alphanumeric information. This column can contain designations for samples that are below the limit of quantitation (e.g. BLQ, \<LLOQ, etc.), missing (e.g. NS, Missing, etc.).

## Analyzed concentration
This column must be in numeric format. Imputations for samples that are below the limit of quantitation or missing must be made in this column. For example, if all BLQ samples are imputed with 0, then a value of 0 should appear in the Analyzed concentration column for each BLQ sample.
