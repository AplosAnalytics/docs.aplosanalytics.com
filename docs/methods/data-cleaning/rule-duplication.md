### Duplication Rule (`duplication`)

Handles duplicate records in the dataset for the input conditions.

| Field          | Description                                       | Required |
| -------------- | ------------------------------------------------- | -------- |
| `columns`      | Column to duplicate                               | ✅ Yes   |
| `sort`         | Array of columns with which to sort by            | ✅ Yes   |
| `duplicate_on` | Field to determine duplication groups             | ✅ Yes   |
| `direction`    | Direction of duplication (forward or backward)    | ✅ Yes   |
| `conditions`   | Conditions to operate against                     | ✅ Yes   |
| `mapping`      | Array of one to many source and duplicate records | ✅ Yes   |

#### Example:

```json
{
  "type": "duplication",
  "columns": {
    "unique_id": "subject"
  },
  "sort": ["day_int", "atime"],
  "duplicate_on": "day_int",
  "direction": "reverse",
  "conditions": [
    {
      "expressions": [
        {
          "column": "time",
          "value": 0,
          "operator": "=="
        }
      ]
    }
  ],
  "mapping": [
    {
      "source_record": {
        "column": "atime"
      },
      "duplicate_record": {
        "column": "atime"
      }
    },
    {
      "source_record": {
        "column": "atime"
      },
      "duplicate_record": {
        "column": "time"
      }
    },
    {
      "source_record": {
        "column": "conc"
      },
      "duplicate_record": {
        "column": "conc"
      }
    },
    {
      "source_record": {
        "column": "conc.obs"
      },
      "duplicate_record": {
        "column": "conc.obs"
      }
    },
    {
      "source_record": {
        "text": "Duplicate"
      },
      "duplicate_record": {
        "column": "record_type"
      }
    }
  ]
}
```

**Behavior:** Processes duplicate records based on subject and configured time value condition.
