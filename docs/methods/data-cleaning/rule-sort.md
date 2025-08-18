### Sorting Rule (`sort`)

Sorts the DataFrame by specified columns.

| Field | Description | Required |
|--------|------------|----------|
| `columns` | Array of column names to sort by | ✅ Yes |
| `ascending` | Sort order (true for ascending, false for descending) | ❌ No (default: true) |

#### Example:
```json
{
    "type": "sort",
    "columns": ["timestamp", "customer_id"],
    "ascending": true
}
```
**Behavior:** Sorts data by timestamp and customer ID in ascending order.