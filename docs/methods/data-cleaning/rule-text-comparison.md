### Text Comparison Rule (`text_comparison`)

Performs comparison of text values in 2 columns and creates a flag for data in a third column.

| Field | Description | Required |
|--------|------------|----------|
| `reference_column` | Column containing the reference values | ✅ Yes |
| `comparison_column` | Column containing the comparison values | ✅ Yes |
| `destination_column` | Column that will be populated with the `matched_value` or `unmatched_value` | ✅ Yes |
| `operator` | Use `==` to test if `reference_column` is equal to `comparison_column`. Use `!=` to test if `reference_column` is not equal to `comparison_column` | ✅ Yes |
| `matched_value` | Numeric value placed in `destination_column` if the comparison is true. | ✅ Yes |
| `unmatched_value` | Numeric value placed in `destination_column` if the comparison is not true. | ✅ Yes |

#### Example:
```json
{
    "type": "text_comparison",
    "reference_column": "sex",
    "operator": "==",
    "comparison_column": "female",
    "destination_column": "sexn",
    "matched_value": 1,
    "unmatched_value": 0
}
```
**Behavior:** If the text in `sex` column matches text in `female` column, the `sexn` column is populated with a 1, otherwise it is populated with a 0.
