### Minimum Value Rules (`min_value`)

Set a minimum threshold for values. If a value is detected to be below the threshold, it will be set to the threshold value.

| Field | Description | Required |
|--------|------------|----------|
| `cap` or `min_threshold` | Minimum allowed value | ✅ Yes |

#### Example:
```json
{
    "type": "min_value",
    "source_column": "rating",
    "destination_column": "",
    "cap": 1
}
```
**Behavior:** Ensures all ratings are at least 1, replacing any lower values.