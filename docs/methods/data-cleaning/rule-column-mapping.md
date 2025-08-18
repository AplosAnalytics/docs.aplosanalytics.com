### Mapping Rule (`mapping`)

Maps data from source columns to destination columns.

| Field | Description | Required |
|--------|------------|----------|
| `columns` | Array of mapping objects with source and destination columns | ✅ Yes |

#### Example:
```json
{
    "type": "mapping",
    "columns": [
        {"source_column": "first_name", "destination_column": "fname"},
        {"source_column": "last_name", "destination_column": "lname"}
    ]
}
```
**Behavior:** Copies data from `first_name` to `fname` and `last_name` to `lname`.