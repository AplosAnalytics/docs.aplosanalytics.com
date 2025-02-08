# 🔵 Data Columns Configuration

A description of each setting on the Data Columns configuration screen is below:

|Field name|Description|Required?|
|:---|:---|:---|
|Time|Sample time for analysis|Required|
|Unique ID|Unique identifier for each subject or animal. If there are multiple profiles for a single subject (e.g. mutliple formulations), use the Grouping variables also.|Required|
|Concentration Observed|Observed concentration that includes text designations for samples below the limit of quantitation or missing samples|Required|
|Concentration Analyzed|Concentration to be used in the calculation of PK parameters. Imputations for missing samples and/or samples below the limit of quantation must be made in this column|Required|
|Grouping variables|Any grouping variables needed to define unique PK profiles for analysis|1 column is required, additional columns are optional. For sparse data, Unique ID is ignored as a grouping variable, and thus at least one other grouping variable must be provided.|
|Sorting|This is how the data is sorted prior to analysis for each unique profile. Generally include the time column variable. This column has been removed from the web user interface as it is generally not needed.|1 column is required, additional columns are optional|
|Custom/Carry Along Values|These are columns with information that will be added to the output files, but is not used group grouping. All grouping variables are automatically added as Custom variables during the analysis by the Aplos NCA engine. This ensures that all grouping variables are included in the output datasets.|Optional|
|Exclusion Column|This column is used to exclude data from the analysis. Select the column that has the exclusion codes.|Optional|
|Exclusion Code|This is the code for exclusions within the selected exclusion column. For example, it may be "N" or it may be the number "1". Only a single exclusion code is permitted. |Optional. Required if Exclusion column is selected.|

**Figure 1: Columns configuration input screen**
<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7818627450980393; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cm6wi1n1y01q13wrqfnx42w2e?embed_v=2" loading="lazy" title="Column configuration" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

## 
> [!TIP]
> The column headers are imported from the analysis dataset and available from the dropdown lists. You can select multiple values for Grouping, Sorting, and Custom/Carry Along Values. You can de-select those using the dropdown list also. 
>
> The column selected for Time will automatically be populated in the Sorting dropdown. The column selected for Unique ID will automatically be populated in the Grouping dropdown.
