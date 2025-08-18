### Whitespace Trimming Rule (`trim_whitespace`)

Removes leading and trailing whitespace from a text column.

#### Example:
```json
{
    "type": "trim_whitespace",
    "source_column": "email",
    "destination_column": ""
}
```
**Behavior:** Removes extra spaces from the `email` column.