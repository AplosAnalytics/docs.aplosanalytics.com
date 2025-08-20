### Exclusion Rules (`exclusion`, `exclusions`)

Excludes values based on specified criteria.

| Field | Description | Required |
|--------|------------|----------|
| `column` | Name of the new column to exclude from | ✅ Yes |
| `value` | Value to exclude | ✅ Yes |

#### Example:
```json
{
  "type": "exclusion",
  "column": "time",
  "value": 1
}
```
**Behavior:** Excludes all time values that equal 1.