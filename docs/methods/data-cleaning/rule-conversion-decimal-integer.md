### Convert Decimal to Integer Rule (`round_float_to_int`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmql68a5b06rpqms4x9jgsrw6?embed_v=2&utm_source=embed" loading="lazy" title="Convert Decimal to Integer" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

Converts data in a column from decimal to integer. May be useful to combine this with Column Mapping rule to convert a copy of the original column.

| Field | Description | Required |
|--------|------------|----------|
| `conversions` | Array of columns to be converted from decimal to integer | ✅ Yes |
| `column` | Columns in dataset to be converted | ✅ Yes |
| `rounding` | Type of rounding to be used. `round` uses standard rounding rules to next highest integer for 5 - 9 and prior integer for 1 - 4; `floor` rounds down to nearest integer; `ceiling` round up to nearest integer; `truncate` drops decimal and retains integer  | ✅ Yes |

#### Example:
```json
{
  "description": "Convert decimal to integer Description",
  "version": "3.0.0",
  "conversions": [
    {
      "column": "dose",
      "rounding": "round"
    }
  ],
  "type": "round_float_to_int"
}
```
**Behavior:** The column `dose` is converted to an integer using standard rounding of any decimals.