### Duplication Rule (`duplication`)

Handles duplicate records in the dataset for the input conditions.

| Field | Description | Required |
|--------|------------|----------|
| `conditions` | Conditions to operate against | ✅ Yes |
| `columns` | Column to duplicate as well as destination | ✅ Yes |
| `sort` | Array of columns with which to sort by | ✅ Yes |
| `duplicate_on` | Field to determine duplication groups | ✅ Yes |

#### Example:

```json
{
  "type": "duplication",
  "conditions": [
    {
      "expressions": [
        {
          "column": "age",
          "operator": ">",
          "value": 18
        }
      ]
    }
  ],
  "columns": {
    "source": "name",
    "destination": "duplicated_name"
  },
  "sort": [],
  "duplicate_on": ""
}
```

**Behavior:** Processes duplicate records based on customer ID.
