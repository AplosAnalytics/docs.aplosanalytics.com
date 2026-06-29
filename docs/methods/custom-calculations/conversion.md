### Conversion (`conversion`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqtqmkap227dqmjaj3v11k73?embed_v=2&utm_source=embed" loading="lazy" title="Conversion - Custom Calculation" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Performs an arithmetic conversion of an existing parameter.

| Field | Description | Required |
|--------|------------|----------|
| `parameter` | Name of the new parameter to be included in the `param` column of the output file | ✅ Yes |
| `paramcd` | Parameter code for the new parameter to be included in the `paramcd` column of the output file. Only alphanumeric characters and underscore (_) are allowed.  | ✅ Yes |
| `uniqueId` | Unique ID variable in the input file. | ✅ Yes |
| `units` | Units of the new parameter | ✅ Yes |
| `paramcd` | Parameter code for the original parameter to be converted. | ✅ Yes |
| `column` | Column of input file for condition matching. | ✅ Yes |
| `value` | Value of `column` to be matched for data filtering (if under `term1` - `conditions`), or value for conversion factor (if under `term2`)| ✅ Yes |
| `operator` | Arithmetic operator for conversion. Accepted values are `+`, `-`, `*`, and `/` | ✅ Yes |

## 
> [!TIP]
> All conversions are calculated as follows:
>  - new parameter = [term1] [operator] [term2]
>  - where [term1] is a parameter from the input file and [term2] is a conversion factor 
> 
> If you need to perform a calculation such as 1 - [parameter], use the addition operator and a negative value for [term2].
> 


#### Example:
```json
{
  "description": "Conversion Calculation Description",
  "version": "3.0.0",
  "parameter": "Apparent Clearance (linear) in liters/hr",
  "paramcd": "CL_f_lin_liter",
  "uniqueId": "subject",
  "units": "L/hr",
  "term1": {
    "paramcd": "CL_f_lin",
    "conditions": [
      {
        "column": "day",
        "value": "Day 1"
      }
    ]
  },
  "operator": "/",
  "term2": {
    "value": 1000
  },
  "type": "conversion"
}
```
**Behavior:** Creates a new parameter named `Apparent Clearance (linear) in liters/hr` using the following equation: new parameter = CL_f_lin / 1000.