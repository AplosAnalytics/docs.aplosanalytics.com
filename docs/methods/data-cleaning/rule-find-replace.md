### Find & Replace Rule (`find_replace`)

Replaces occurrences of a specified value in a column.

| Field | Description | Required |
|--------|------------|----------|
| `find` | The text or pattern to search for. | ✅ Yes |
| `replace` | The text to replace matches with. | ✅ Yes |
| `regex` | If `true`, the `find` field will be treated as a regular expression. | ❌ No (default: `false`) |

#### Example:
```json
{
    "type": "find_replace",
    "source_column": "customer_name",
    "destination_column": "",
    "find": "Inc\.",
    "replace": "Incorporated",
    "regex": true
}
```
**Behavior:** Replaces "Inc." with "Incorporated" in the `customer_name` column.