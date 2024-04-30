# Optional Columns
Aplos NCA supports both grouping columns and custom columns. Grouping and Custom columns can contain any alphanumeric information; however, the values should be the same for each unique profile for a single subject. You may specify as many grouping or custom columns as needed. Examples of variables that could be used for grouping or custom columns are listed below:

 -   Sex
 -   Treatment
 -   Formulation
 -   Period
 -   Dose level

## Grouping Columns
Grouping columns are used to group data together if the subject identifier variable is not unique for each profile. For example, in a two-way crossover study, a subject receives two different treatments. Therefore, the subject identifier alone is not adequate to define a single profile. The column that contians the treatment assignement should be included as a grouping variable. 

Grouping columns are also used to summarize the results. Any grouping variable will be used to create summary plots and tables based on each unique value in the grouping column. For example, Sex can be included as a Grouping column to get separate summaries for Male and Female.

A summary is produced for each level of each grouping variable, and all combinations of grouping variable levels when there are more than one. Therefore, it is strongly recommended to only include Grouping columns for which a summary is necessary. 

## Custom Columns
Custom columns are not required for grouping data, but will be carried through to the results. For example, in a a randomized two-way crossover study a user could set Treatment as a Grouping column and include Period as a Custom column. The Period will be included in the outputs eventhough it is not necessary for grouping data together.   