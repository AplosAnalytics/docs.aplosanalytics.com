### Numerical Formatting Rule (`numerical_format`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqlr48360oksqms48wfedszo?embed_v=2&utm_source=embed" loading="lazy" title="Numerical Formatting (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Formats numerical data by using either significant digits or decimal places. May be useful to combine this with Column Mapping rule to convert a copy of the original column.

| Field | Description | Required |
|--------|------------|----------|
| `column` | Column in dataset to be converted | ✅ Yes |
| `formatType` | Significant digits `digits` or decimal places `decimal` | ✅ Yes |
| `number` | Integer value that specifies the number of significant digits or decimal places. | ✅ Yes |

#### Example:
```json
{
  "description": "Numerical Formatting Description",
  "version": "3.0.0",
  "column": "conc",
  "formatType": "digits",
  "number": 2,
  "type": "numerical_format"
}
```
**Behavior:** The column `conc` is formatted with 2 significant digits.