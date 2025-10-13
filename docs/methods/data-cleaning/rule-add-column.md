### Add Column Rule (`add_column`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgh2w6297vku2nomq2mimdvo?embed_v=2&utm_source=embed" loading="lazy" title="Add Column (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Adds a new column with a specified default value.

| Field | Description | Required |
|--------|------------|----------|
| `column_name` | Name of the new column to add | ✅ Yes |
| `default_value` | Default value for the new column | ✅ Yes |

#### Example:
```json
{
    "type": "add_column",
    "column_name": "processed_flag",
    "default_value": true
}
```
**Behavior:** Adds a new column `processed_flag` with default value `true` for all rows.