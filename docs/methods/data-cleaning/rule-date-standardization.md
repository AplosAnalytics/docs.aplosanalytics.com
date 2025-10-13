### Date Standardization Rule (`date_standardization`)

<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.7604790419161678; padding: 40px 0 40px 0;"><iframe src="https://guides.aplosanalytics.com/embed/cmgiarpp80eh8krn9mkj5wczy?embed_v=2&utm_source=embed" loading="lazy" title="Date Standardization (Data cleaning)" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Converts date formats from one pattern to another.

| Field | Description | Required |
|--------|------------|----------|
| `current_format` | The format of the existing date string (e.g., `"%d-%m-%Y"`). | ✅ Yes |
| `new_format` | The desired output format (e.g., `"%Y-%m-%d"`). | ✅ Yes |

#### Example:
```json
{
    "type": "date_standardization",
    "source_column": "transaction_date",
    "destination_column": "",
    "current_format": "%d-%m-%Y",
    "new_format": "%Y-%m-%d"
}
```
**Behavior:** Converts dates from `"DD-MM-YYYY"` format to `"YYYY-MM-DD"`.
