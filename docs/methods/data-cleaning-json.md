# 📄 Data Cleaning JSON

**This is a beta feature that is currently under development. You may use it, however, you may encounter errors and bugs when using these features.**

Data Cleaning refers to manipulation of the input dataset to create an analysis-ready dataset for the calculation of PK parameters. These manipulations include the addition of new columns to the dataset, conversion of BLQ samples to analyzed values, and preparation of exclusion columns to exclude individual subject profiles or individual records. All data cleaning steps are performed sequentially and at the end of each step the output is saved and included in the final output. Users can verify the results in the output. 

Here are examples of data cleaning rules that can be used along with example JSON code to perform the action. In the future the website user interface will enable creation of the required JSON information. Until the user interface is available, manual creation of the JSON file is the only solution.

The basic JSON structure for data cleaning is shown below. All of the manipulations must be inside of the "rules" array. Each "rule" is executed sequentially.

```json:line-numbers
{
    "data_cleaning":{
        "rules": [

        ]
    }
}
```
### Add a column with a fixed value

The rule for adding a column with a fixed value for each record is shown below. This can be used to add a units column to the dataset which can be used in the analysis for both reporting parameter units and in plots and tables.
```json:line-numbers
{
    "description": "Add time units",
    "type": "add_column",
    "column_name": "time_units",
    "value": "hr"
},
{
    "description": "Add Group value",
    "type": "add_column",
    "column_name": "Group",
    "value": 1
}
```
### Add a column with a value based on another column value**

The rule for adding a column with a value based on another column value in the dataset is shown below. This can be used to add a treatment description based on the a group designation, or adding a dose amount based on a group designation.
```json:line-numbers
{
    "description": "Add Cohort column",
    "type": "find_replace",
    "source_column": "group",
    "destination_column": "Cohort",
    "id": "subject",
    "actions": [
        {
            "find": 1,
            "replace": "Cohort 1"
        },
        {
            "find": 2,
            "replace": "Cohort 2"
        },
        {
            "find": 3,
            "replace": "Cohort 3"
        },
        {
            "find": 4,
            "replace": "Cohort 4"
        }
    ]
}
```

### BLQ handling Option 1

This converts all BLQ samples to 0 in the dataset. This method is often used when users want to plot the data or calculate the mean concentrations at nominal time points. The rule for this BLQ handling is shown below with the assumption that the concentration column includes "BLQ" as the text for samples below the limit of quantitation.
```json:line-numbers
{
    "description": "BLQ Option 1 - set all BLQ to 0",
    "type": "grouping",
    "columns": [
        "subject"
    ]
    "rules": [
        {
            "type": "sort",
            "columns": [
              "time"
            ],
            "direction": "asc"
        },
        {
            "type": "mapping",
            "columns": [
                {
                    "source_column": "concentration",
                    "destination_column": "PKLEVEL1"
                }
            ]
        },
        {
            "type": "conditional",
            "conditions": [
                {
                    "description": "Missing values",
                    "expressions": [
                        {
                            "column": "concentration",
                            "value": "NS",
                            "operator": "=="
                        }
                    ],
                    "action": {
                        "assign": {
                            "column": "PKLEVEL1",
                            "value": ""
                        }
                    }
                },
                {
                    "description": "Concentration == BLQ",
                    "expressions": [
                        {
                            "column": "concentration",
                            "value": "BLQ",
                            "operator": "=="
                        }
                    ],
                    "action": {
                        "assign": {
                            "column": "PKLEVEL1",
                            "value": 0
                        }
                    }
                }
            ]
        }
    ]
}
```

### BLQ handling Option 2

This converts all BLQ samples before the first measurable concentration to 0 and all BLQ samples after the first measurable concentration to "missing" in the dataset. This method is preferred for calculation of PK parameters. The rule for this BLQ handling is shown below with the assumption that the concentration column includes "BLQ" as the text for samples below the limit of quantitation.
```json:line-numbers
{
    "description": "BLQ Option 2 - set BLQ before first measurable concentration to 0 and missing thereafter",
    "type": "grouping",
    "columns": [
        "subject"
    ]
    "rules": [
        {
            "type": "sort",
            "columns": [
              "time"
            ],
            "direction": "asc"
        },
        {
            "type": "mapping",
            "columns": [
                {
                    "source_column": "concentration",
                    "destination_column": "PKLEVEL2"
                }
            ]
        },
        {
            "description": "PKLEVEL2 - set blq flags",
            "type": "blq",
            "source_column": "concentration",
            "destination_column": "BLQ_FLAGS",
            "before": 0,
            "at": 1,
            "after": 2
        },
        {
            "type": "conditional",
            "conditions": [
                {
                    "description": "Missing values",
                    "expressions": [
                        {
                            "column": "concentration",
                            "value": "NS",
                            "operator": "=="
                        }
                    ],
                    "action": {
                        "assign": {
                            "column": "PKLEVEL2",
                            "value": ""
                        }
                    }
                },
                {
                "description": "BEFORE the first numeric concentration",
                "expressions": [
                  {
                    "column": "concentration",
                    "value": "BLQ",
                    "operator": "=="
                  },
                  {
                    "column": "BLQ_FLAGS",
                    "value": 0,
                    "operator": "=="
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL2",
                    "value": 0
                  }
                }
              },
              {
                "description": "BEFORE the first numeric concentration - catches NO TMAX value",
                "expressions": [
                  {
                    "column": "BLQ_FLAGS",
                    "value": "",
                    "operator": "=="
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL2",
                    "value": 0
                  }
                }
              },
              {
                "description": "AFTER the first numeric concentration = BLQ",
                "expressions": [
                  {
                    "column": "concentration",
                    "value": "BLQ",
                    "operator": "=="
                  },
                  {
                    "column": "BLQ_FLAGS",
                    "value": 1,
                    "operator": ">"
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL2",
                    "value": ""
                  }
                }
              }
            ]
        }
    ]
}
```

### BLQ handling Option 3

This converts all BLQ samples before Tmax to 0 and all BLQ samples after Tmax to "missing" in the dataset. This method can be used for calculation of PK parameters. The rule for this BLQ handling is shown below with the assumption that the concentration column includes "BLQ" as the text for samples below the limit of quantitation.
```json:line-numbers
{
    "description": "BLQ Option 3 - set BLQ before Tmax to 0 and missing thereafter",
    "type": "grouping",
    "columns": [
        "subject"
    ]
    "rules": [
        {
            "type": "sort",
            "columns": [
              "time"
            ],
            "direction": "asc"
        },
        {
            "description": "Set up column for Cmax",
            "type": "max",
            "source_column": "concentration",
            "destination_column": "CMAX"
        },
        {
            "description": "Set up column for Tmax flag",
            "type": "add_column",
            "column_name": "TMAX_FLAG",
            "value": 0
        },
        {
            "description": "Create Tmax flags",
            "type": "tmax_timepoints_up_down",
            "compare_column": "CMAX",
            "source_column": "concentration",
            "destination_column": "TMAX_FLAG"
        },
        {
            "type": "mapping",
            "columns": [
                {
                    "source_column": "concentration",
                    "destination_column": "PKLEVEL3"
                }
            ]
        },
        {
            "type": "conditional",
            "conditions": [
                {
                    "description": "Missing values",
                    "expressions": [
                        {
                            "column": "concentration",
                            "value": "NS",
                            "operator": "=="
                        }
                    ],
                    "action": {
                        "assign": {
                            "column": "PKLEVEL3",
                            "value": ""
                        }
                    }
                },
                {
                "description": "BEFORE Tmax",
                "expressions": [
                  {
                    "column": "concentration",
                    "value": "BLQ",
                    "operator": "=="
                  },
                  {
                    "column": "TMAX_FLAG",
                    "value": 0,
                    "operator": "=="
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL3",
                    "value": 0
                  }
                }
              },
              {
                "description": "BEFORE TMAX - catches NO TMAX value",
                "expressions": [
                  {
                    "column": "TMAX_FLAG",
                    "value": "",
                    "operator": "=="
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL3",
                    "value": 0
                  }
                }
              },
              {
                "description": "AFTER TMAX = BLQ",
                "expressions": [
                  {
                    "column": "concentration",
                    "value": "BLQ",
                    "operator": "=="
                  },
                  {
                    "column": "TMAX_FLAG",
                    "value": 1,
                    "operator": ">="
                  }
                ],
                "action": {
                  "assign": {
                    "column": "PKLEVEL3",
                    "value": ""
                  }
                }
              }
            ]
        }
    ]
}
```

