### Numeric Comparison Rule (`numeric_comparison`)

Performs comparison of numeric values in 2 columns and creates a flag for data in a third column.

| Field | Description | Required |
|--------|------------|----------|
| `reference_column` | Column containing the reference values | ✅ Yes |
| `comparison_column` | Column containing the comparison values | ✅ Yes |
| `destination_column` | Column that will be populated with the `matched_value`, `unmatched_value`, `nonnumerical_reference_value`, `nonnumerical_comparison_value`, or `nonnumerical_values` | ✅ Yes |
| `operator` | Operator for comparison. Available operators are `<`, `<=`, `>`, `>=`, `==`, and `!=`. The operators are used as follows `reference_column` value [operator] `comparison_column` value. | ✅ Yes |
| `matched_value` | Numeric value placed in `destination_column` if the comparison is true. | ✅ Yes |
| `unmatched_value` | Numeric value placed in `destination_column` if the comparison is not true. | ✅ Yes |
| `nonnumerical_reference_value` | Numeric value placed in `destination_column` if the value in the `reference_column` is not numeric. | ✅ Yes |
| `nonnumerical_comparison_value` | Numeric value placed in `destination_column` if the value in the `comparison_column` is not numeric. | ✅ Yes |
| `nonnumerical_values` | Numeric value placed in `destination_column` if the values in both the `reference_column` and `comparison_column` are not numeric. | ✅ Yes |

#### Example:
```json
{
    "type": "numeric_comparison",
    "reference_column": "dose",
    "operator": "<",
    "comparison_column": "dose2",
    "destination_column": "dose_comparison",
    "matched_value": 1,
    "unmatched_value": 0,
    "nonnumerical_reference_value": -99,
    "nonnumerical_comparison_value": -98,
    "nonnumerical_values": -97
}
```
**Behavior:** If the value in `dose` column is less than the value in `dose2` column, the `dose_comparison` column is populated with a 1, otherwise it is populated with a 0. If the value in the `dose` column is not numeric, but the value in the `dose2` column is numeric, the `dose_comparison` column will be populated with -99. If the value in the `dose` column is numeric and the value in the `dose2` column is not numeric, the `dose_comparison` column will be populated with -98. If the values in both the `dose` and `dose2` columns are not numeric, the `dose_comparison` column will be populated with -97.
