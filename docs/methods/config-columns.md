# Data Columns Configuration
![Column configuration input](./images/Columns_input.png)

A description of each setting on the Data Columns configuration screen is below:

|Field name|Description|
|:---|:---|
|Time|Sample time for analysis|
|Unique ID|Unique identifier for each subject or animal. If there are multiple profiles for a single subject (e.g. mutliple formulations), use the Grouping variables also.|
|Concentration Observed|Observed concentration that includes text designations for samples below the limit of quantitation or missing samples|
|Concentration Analyzed|Concentration to be used in the calculation of PK parameters. Imputations for missing samples and/or samples below the limit of quantation must be made in this column|
|Grouping variables|Any grouping variables needed to define unique PK profiles for analysis|
|Sorting|This is how the data is sorted prior to analysis for each unique profile. Generally include the time column variable|
|Custom/Carry Along Values|These are columns with information that will be added to the output files, but is not used group grouping.|