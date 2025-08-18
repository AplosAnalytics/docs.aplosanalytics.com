### BLQ Rule (`blq`)

Handles Below Limit of Quantification (BLQ) values in pharmacokinetic data.

| Field | Description | Required |
|--------|------------|----------|
| `before` | Value to use before TMAX | ✅ Yes |
| `at` | Value to use at TMAX | ✅ Yes |
| `after` | Value to use after TMAX | ✅ Yes |

#### Example:
```json
{
    "type": "blq",
    "source_column": "concentration",
    "destination_column": "blq_flag",
    "before": 0,
    "at": 1,
    "after": 2
}
```
**Behavior:** Sets BLQ flags based on position relative to TMAX.