### Null Replacement Rule (`null_replacement`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgpdipey0v3a12sxtxxm9d5i?embed_v=2&utm_source=embed" loading="lazy" title="Null replacement (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Replaces `null` or missing values with a default value.

| Field | Description | Required |
|--------|------------|----------|
| `replacement_value` | The value to use when the source column is `null` or empty. | ✅ Yes |

#### Example:
```json
{
    "type": "null_replacement",
    "source_column": "age",
    "destination_column": "",
    "replacement_value": 0
}
```
**Behavior:** If the `age` column is `null`, it will be replaced with `0`.