### Sparse Data Rule (`sparse_data`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqlracpm0ommqms46vtay1tp?embed_v=2&utm_source=embed" loading="lazy" title="Sparse Data Rule (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Sparse data calculates mean concentrations for sparse sampling designs. User specified grouping variables, time variable, and concentration variable. This function then calculates the mean and standard deviation at each time point. This data can now be used for PK analysis. Note that this rule must be the last rule in a data cleaning pipeline.

| Field | Description | Required |
|--------|------------|----------|
| `groupingColumns` | Array of columns to be used to group the data for summarization | ✅ Yes |
| `timeColumn` | Column that includes the time variable | ✅ Yes |
| `concentrationColumn` | Column that includes the concentration data for summarization. Should be a column with only numeric values.  | ✅ Yes |
| `groupIdColumnName` | New column in output that will contain group id numbers  | ✅ Yes |
| `carryAlongColumns` | Columns for which data will be carried into the output file. Only the first value in each profile will be used | ❌ No  |
| `uniqueId` | Column that contains unique subject identifiers | ✅ Yes |
| `includedIdsColumnName` | New column in output that will contain unique subject identifiers used in the summarization | ✅ Yes |

#### Example:
```json
{
  "description": "Sparse Data Description",
  "version": "3.0.0",
  "groupingColumns": [
    "sex",
    "dose"
  ],
  "timeColumn": "time",
  "concentrationColumn": "conc",
  "groupIdColumnName": "group_id",
  "carryAlongColumns": [
    "dose"
  ],
  "uniqueId": "subject",
  "includedIdsColumnName": "subjects_included",
  "type": "sparse_data"
}
```
**Behavior:** Concentration data in `conc` will be summarized by `dose` and `sex` at each timepoint in `time`. The new group identifiers will be in `group_id`, and included subjects for each summary time point will be in `subjects_included`.