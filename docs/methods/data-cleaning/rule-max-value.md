### Maximum Value Rules (`max_value`)

Cap values at a specified maximum threshold. If a value is detected to be above the threshold, it will be set to the threshold value.

| Field | Description | Required |
|--------|------------|----------|
| `cap` or `max_threshold` | Maximum allowed value | ✅ Yes |
| `max_value` | Value to use when threshold is exceeded | ❌ No (defaults to threshold) |

#### Example:
```json
{
    "type": "max_value",
    "source_column": "score",
    "destination_column": "",
    "cap": 100
}
```
**Behavior:** Caps all scores at 100, replacing any higher values.