### Ratio (`ratio`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqtmj9ed1u1pqmjax9km4rry?embed_v=2&utm_source=embed" loading="lazy" title="Ratio Calculations" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Calculates the ratio of two parameters.

| Field | Description | Required |
|--------|------------|----------|
| `parameter` | Name of the new parameter to be included in the `param` column of the output file | ✅ Yes |
| `paramcd` | Parameter code for the new parameter to be included in the `paramcd` column of the output file. Only alphanumeric characters and underscore (_) are allowed.  | ✅ Yes |
| `uniqueId` | Unique ID variable in the input file. | ✅ Yes |
| `numerator` | Specifications for the parameter to be used as the numerator in the ratio calculation. | ✅ Yes |
| `denominator` | Specifications for the parameter to be used as the denominator in the ratio calculation. | ✅ Yes |
| `paramcd` | Parameter code for input file parameter to be used as either the numerator or denominator. | ✅ Yes |
| `column` | Input data file column to be used in a `condition` to filter the data. | ✅ Yes |
| `value` | Value in the input data file in the selected `column` to filter the data. | ✅ Yes |

#### Example:
```json
{
  "parameter": "Relative Bioavailability (AUCall)",
  "description": "Relative BA - AUCall",
  "paramcd": "Frel_AUCall",
  "type": "ratio",
  "uniqueId": "subject",
  "numerator": {
    "conditions": [
      {
        "column": "trta",
        "value": "Fed"
      }
    ],
    "paramcd": "AUC_all_lin"
  },
  "denominator": {
    "conditions": [
      {
        "column": "trta",
        "value": "Fasted"
      }
    ],
    "paramcd": "AUC_all_lin"
  }
}
```

## 
> [!TIP]
> You may include as many conditions as needed to uniquely identify the parameter. 
>


**Behavior:** Creates a new parameter `Relative Bioavailability (AUCall)` by dividing AUC_all_lin in the Fed state by AUC_all_lin in the Fasted state.