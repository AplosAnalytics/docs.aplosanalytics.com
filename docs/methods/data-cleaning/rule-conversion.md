### Arithmetic Conversion Rule (`conversion`)

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