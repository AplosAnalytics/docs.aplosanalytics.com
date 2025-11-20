### Convert String to Numeric Rule (`convert_types`)

Converts data in a column from string to numeric. Anything that cannot be converted to numeric in the column will be converted to NA (missing). May be useful to combine this with Column Mapping rule to convert a copy of the original column.

| Field | Description | Required |
|--------|------------|----------|
| `conversions` | Array of columns to be converted from string to numeric | ✅ Yes |
| `column` | Columns in dataset to be converted | ✅ Yes |
| `to_type` | Type of number can be either an integer (`int`) or decimal (`float`) | ✅ Yes |

#### Example:
```json
{
    "type": "convert_types",
    "conversions": [
        {
            "column": "day",
            "to_type": "int"
        },
        {
            "column": "amount",
            "to_type": "float"
        }
    ]
}
```
**Behavior:** The column `day` is converted to an integer and the column `amount` is converted to decimal. Any non-numeric values are converted to missing.