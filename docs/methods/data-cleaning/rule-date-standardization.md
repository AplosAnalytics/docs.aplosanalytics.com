### Date Standardization Rule (`date_standardization`)

Converts date formats from one pattern to another.

| Field | Description | Required |
|--------|------------|----------|
| `current_format` | The format of the existing date string (e.g., `"%d-%m-%Y"`). | ✅ Yes |
| `new_format` | The desired output format (e.g., `"%Y-%m-%d"`). | ✅ Yes |

#### Example:
```json
{
    "type": "date_standardization",
    "source_column": "transaction_date",
    "destination_column": "",
    "current_format": "%d-%m-%Y",
    "new_format": "%Y-%m-%d"
}
```
**Behavior:** Converts dates from `"DD-MM-YYYY"` format to `"YYYY-MM-DD"`.
