### Grouping Rule (`grouping`)

Groups data by specified columns and applies sub-rules to each group.

| Field | Description | Required |
|--------|------------|----------|
| `columns` | Array of column names to group by | ✅ Yes |
| `rules` | Array of sub-rules to apply to each group | ✅ Yes |

#### Example:
```json
{
    "type": "grouping",
    "columns": ["customer_id", "product_type"],
    "rules": [
        {"type": "trim_whitespace", "source_column": "description"}
    ]
}
```
**Behavior:** Groups data by customer and product type, then applies whitespace trimming to each group.