### Time Zero Rule (`time_zero`)

Handles time zero adjustments in pharmacokinetic data.

#### Example:
```json
{
    "type": "time_zero",
    "source_column": "time",
    "destination_column": "adjusted_time"
}
```
**Behavior:** Adjusts time values relative to time zero.