### Conditional Rule (`conditional`)

Applies conditional logic to determine values based on specified conditions.

| Field        | Description                           | Required |
| ------------ | ------------------------------------- | -------- |
| `conditions` | Array of condition objects with logic | ✅ Yes   |

#### Example:

```json
{
  "type": "conditional",
  "conditions": [
    {
      "expressions": [
        {
          "column": "age",
          "operator": "<",
          "value": 18
        }
      ],
      "action": {
        "assign": {
          "column": "age_group",
          "value": "minor"
        }
      }
    },
    {
      "expressions": [
        {
          "column": "age",
          "operator": ">=",
          "value": 18
        }
      ],
      "action": {
        "assign": {
          "column": "age_group",
          "value": "adult"
        }
      }
    }
  ]
}
```

**Behavior:** Populates the age_group column with a value based on the minor and adult conditions.
