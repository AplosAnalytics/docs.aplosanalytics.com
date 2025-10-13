### Conditional Rule (`conditional`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgi3ins201y1krn9maxc1co7?embed_v=2&utm_source=embed" loading="lazy" title="Conditional Rule (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

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
