### Regular Expression Rule (`regex`)

Extracts data using regular expression patterns.

| Field | Description | Required |
|--------|------------|----------|
| `pattern` | Regular expression pattern to match | ✅ Yes |

#### Example:
```json
{
    "type": "regex",
    "source_column": "email",
    "destination_column": "domain",
    "pattern": "@([^.]+\\.[^.]+)$"
}
```
**Behavior:** Extracts the domain from email addresses.