# 🟤 Partial AUC

Partial AUCs are user-defined ranges for calculation of area under the curve. The user must define the following information for each partial AUC to be calculated:

* **Name**: This is what will appear in the output in the "param" column. Normally this is a clear explanation of the parameter such as "Partial AUC0-4 hours"
* **Code**: This is what will appear in the output in the "paramcd" column. Normally this is an abbreviation to unqiuely identify the parameter when using coding. One example could be "pAUC4".
* **Start**: This is the start time for the partial AUC. This value is assumed to be in the same units as the time variable in the dataset.
* **End**: This is the end time for the partial AUC. This value is assumed to be in the same units as the time variable in the dataset.

## Calculation method

The partial AUC is calculated using both the [linear trapezoidal method](../aucmethods) and the [linear up log down trapezoidal method](../aucmethods). If either the start time or end time for the partial AUC is present in the profile, the observed concentrations (and all observed concentrations in between) will be used for the calculation of the partial AUC. If the start time or end time is not present in the profile, the concentration will be imputed using [linear interpolation](../extrapolationmethods) between the two adjacent time points. The imputed concentrations will then be used for the partial AUC calculation. The imputed concentration values are not provided in the output. If the start time is before the first observation or the end time is after the last observation the partial AUC will not be calculated for that individual.

> [!NOTE]
> If the end time extends beyond the available data the partial AUC will not be calculated and will be reported in the non-fatal error text file in the output. For example, if the final observed value is at 23.5 hours and you ask for the partial AUC from 0 - 24 hours, it will not be calculated. 

## Input for web configuration
<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqspy0hu0jilqmjalpbv4ocd?embed_v=2&utm_source=embed" loading="lazy" title="PK Analysis - Partial AUCs" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>


## Manual JSON structure
If you are performing analysis using a formatted JSON file, you must structure the partial AUC using standard JSON structures. The "partial_auc" section is at the top level of the configuration JSON. An example with 2 partial AUCs is below:

```js
{
  "partial_auc": [
    {
      "name": "Partial AUC0-4 hours",
      "code": "pAUC4",
      "start": 0,
      "end": 4
    },
    {
      "name": "Partial AUC4-8 hours",
      "code": "pAUC8",
      "start": 4,
      "end": 8
    }
  ]
}
```


