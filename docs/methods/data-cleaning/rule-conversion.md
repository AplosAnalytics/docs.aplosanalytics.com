### Arithmetic Conversion Rule (`conversion`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgi9m18f0cf4krn9zwdvc1ye?embed_v=2&utm_source=embed" loading="lazy" title="Arithmetic conversion (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Performs arithmetic operations on column values using operators (+, -, *, /).

| Field | Description | Required |
|--------|------------|----------|
| `operator` | The arithmetic operator: "+", "-", "*", or "/" | ✅ Yes |
| `value` | The numeric value to use in the operation | ✅ Yes (if `column` not specified) |
| `column` | Alternative column to use as the second operand | ✅ Yes (if `value` not specified) |

#### Example:
```json
{
    "type": "conversion",
    "source_column": "hours",
    "destination_column": "minutes",
    "operator": "*",
    "value": 60
}
```
**Behavior:** Multiplies values in the `hours` column by 60 and stores the result in the `minutes` column.