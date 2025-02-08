# 📄 Configuration JSON

The following is an example of a configuration JSON file. You can copy and paste this into a text editor, then make changes that match your analysis dataset.

```json:line-numbers
{
    "output": {
        "maximum_precision": false
    },
    "kel_rules": {
        "minimum_span": 0,
        "tie": [
            "kel_n",
            "kel_lower"
        ],
        "earliest_time_point": 0,
        "maximum_extrapolation_linear": 0,
        "maximum_time_points": 0,
        "minimum_statistic": 0,
        "maximum_extrapolation_logarithmic": 0,
        "regression_statistic": "adj_r2"
    },
    "designations": {
        "missing": {
            "comment": "Use either column or value, but not both. If you use column, that header must exist in the dataset.",
            "column": "missing_code",
            "value": "NS"
        },
        "blq": {
            "comment": "Use either column or value, but not both. If you use column, that header must exist in the dataset.",
            "column": "blq_code",
            "value": "BLQ"
        },
        "concentration_unit": {
            "comment": "Use either column or value, but not both. If you use column, that header must exist in the dataset.",
            "column": "conc_unit",
            "value": "ng/mL"
        }
    },
    "columns": {
        "concentration": {
            "analyzed": "conc",
            "observed": "conc.obs"
        },
        "time": "time",
        "unique_id": "subject",
        "custom_columns": [
            "day",
            "freq"
        ],
        "grouping": [
            "subject",
            "day",
            "freq"
        ],
        "sorting": [
            "time"
        ]
    },
    "partial_auc": [
        {
            "name": "Partial AUC0-4 hours",
            "code": "pAUC4",
            "start": 0,
            "end": 4
        },
        {
            "name": "Partial AUC4-8 hours",
            "code": "pAUC8",
            "start": 4,
            "end": 8
        }
    ],
    "sparse_data": false,
    "exclusions": {
        "column_name": "",
        "exclusion_code": "",
        "inclusion_code": ""
    },
    "time": {
        "tau": {
            "comment": "Use column or value, but not both.",
            "column": "tau",
            "value": 24
        },
        "unit": {
            "comment": "Use column or value, but not both.",
            "column": "time_unit",
            "value": "hr"
        },
        "infusion": {
            "protocol": {
                "comment": "Use column or value, but not both. Acceptable inputs are rate or duration.",
                "column": "infusion_type",
                "value": "rate"
            },
            "amount": {
                "comment": "Use column or value, but not both.",
                "column": "infusion_rate",
                "value": 1
            },
        },
        "time_of_administration": {
            "comment": "Use column or value, but not both.",
            "column": "time_dose",
            "value": 0
        }
    },
    "dosing": {
        "amount": {
            "comment": "Use column or value, but not both.",
            "column": "dose",
            "value": 100
        },
        "unit": {
            "comment": "Use column or value, but not both.",
            "column": "dose_units",
            "value": "mg"
        },
        "type": {
            "comment": "Use column or value, but not both. Acceptable inputs are ev, iv-bolus, iv-infusion.",
            "column": "route",
            "value": "ev"
        },
        "frequency": {
            "comment": "Use column or value, but not both. Acceptable inputs are single or steady-state.",
            "column": "freq",
            "value": "single"
        }
    },
    "version": "2024-02-22"
}
```
## 
> [!TIP]
> Comments are for explanation only and can be removed from the JSON file for submission.
