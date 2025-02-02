# ❓ Optional Columns
Aplos NCA supports both grouping columns and custom columns. Grouping and custom columns can contain any alphanumeric information; however, the values should be the same for each unique profile for a single subject (i.e. time-varying variables are not supported). You may specify as many grouping or custom columns as needed. Examples of variables that could be used for grouping or custom columns are listed below:

 -   Sex
 -   Treatment
 -   Formulation
 -   Period
 -   Dose level

## Grouping Columns
Grouping columns are used to group data together if the subject identifier variable is not unique for each profile. For example, in a two-way crossover study, a subject receives two different treatments. Therefore, the subject identifier alone is not adequate to define a single profile. The column that contains the treatment assignement should be included as a grouping variable. To extend this example, you may include the treatment period as a custom column to be included in the output, but not used to group the data into unique profiles.

Grouping columns are also used to summarize the results. Any grouping variable will be used to create summary plots and tables based on each unique value in the grouping column. For example, Sex can be included as a Grouping column to get separate summaries for Male and Female.

A summary is produced for each level of each grouping variable, and all combinations of grouping variable levels when there are more than one. Analysis time increases with additional grouping variables. Therefore, it is recommended to only include Grouping columns for which a summary is necessary. 

The configuration that is returned with the results will include all grouping variables in the Custom column setting as well. This ensures that all grouping variables are included in output tables. 

When analyzing sparse data (e.g. toxicokinetic studies), the Unique ID variable will be ignored if it is included as a grouping variable. Sparse data is summarized by time points within each group, excluding the Unique ID. At least one grouping variable must be provided for sparse data analysis.

## Custom Columns
Custom columns are not required for grouping data, but will be carried through to the results. For example, in a a randomized two-way crossover study a user could set Treatment as a Grouping column and include Period as a Custom column. The Period will be included in the outputs eventhough it is not necessary for grouping data together.  

## 
> [!TIP]
> Only use grouping variables if you need to:
>  - Generate summaries for a specific group
>  - Use grouping variables to uniquely identify a PK profile for a subject
> 
> Use custom columns for all other variables that you would like to carry along in the output.
