### Add Column Rule (`add_column`)

Adds a new column with a specified default value.

| Field | Description | Required |
|--------|------------|----------|
| `column_name` | Name of the new column to add | ✅ Yes |
| `default_value` | Default value for the new column | ✅ Yes |

#### Example:
```json
{
    "type": "add_column",
    "column_name": "processed_flag",
    "default_value": true
}
```
**Behavior:** Adds a new column `processed_flag` with default value `true` for all rows.