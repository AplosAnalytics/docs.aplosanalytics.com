### Null Replacement Rule (`null_replacement`)

Replaces `null` or missing values with a default value.

| Field | Description | Required |
|--------|------------|----------|
| `replacement_value` | The value to use when the source column is `null` or empty. | ✅ Yes |

#### Example:
```json
{
    "type": "null_replacement",
    "source_column": "age",
    "destination_column": "",
    "replacement_value": 0
}
```
**Behavior:** If the `age` column is `null`, it will be replaced with `0`.