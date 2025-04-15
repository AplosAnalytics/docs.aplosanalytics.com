# 📄 Post Processing JSON

**This is a beta feature that is currently under development. You may use it, however, you may encounter errors and bugs when using these features.**

Post processing includes 4 distinct features that are performed after the NCA parameters are calculated. These are:
1. Calculation of composite parameters (e.g. ratios, unit conversions, etc.)
2. Preparation of custom tables
3. Preparation of custom plots
4. Preparation of custom reports (in Microsoft Word format)

All post-processing activities are performed in the order listed above, regardless of the order presented in the post processing JSON file. The output for these activities are included in separate folders in the download package and can be reviewed for accuracy.

Here are some examples of post processing rules that can be used along with example JSON code to perform the desired action. In the future, the website user interface will enable creation of the required JSON code. Until the user interface is available, manual creation of the JSON file is the only solution for using this feature.

The basic JSON structure for post processing is shown below. Users may include any or all of the different outputs as desired. For example, a user may want to produce a post-analysis calculation, but no tables, plots, or report. While another user may not perform any post-analysis calculations, but would like tables, plots, and a report. Sections that are not needed can be left blank or omitted.

```json:line-numbers
{
    "custom_calculations": {

    },
    "custom_tables": {
        
    },
    "custom_plots": {
        
    },
    "custom_reports": {
        
    }
}
```
### Example of metabolic ratio calculation
Metabolic ratio calculations are used to compare the relative exposure of different metabolites to the parent drug. Normally this is done by taking the ratio of the AUC for the metabolite relative to the parent drug. An example of such a calculation is shown below.

```json:line-numbers
{
    "custom_calculations": {
        "description": "Metabolic ratio",
        "output": {
            "file_name": "pk-addl-params.csv",
            "sort": [
                "subject"
            ]
        },
        "calculations": [
            {
                "description": "Metabolic ratio for AUCall for metabolite 1",
                "type": "ratio",
                "unique_id": "subject",
                "paramcd": "MRAUCall",
                "parameter": "Metabolic Ratio AUCall",
                "numerator": {
                    "paramcd": "AUC_all_log",
                    "conditions": [
                        {
                            "column": "Analyte",
                            "value": "M1"
                        }
                    ]
                },
                "denominator": {
                    "paramcd": "AUC_all_log",
                    "conditions": [
                        {
                            "column": "Analyte",
                            "value": "Parent"
                        }
                    ]
                },
            },
            {
                "description": "Metabolic ratio for AUCall for metabolite 2",
                "type": "ratio",
                "unique_id": "subject",
                "paramcd": "MRAUCall",
                "parameter": "Metabolic Ratio AUCall",
                "numerator": {
                    "paramcd": "AUC_all_log",
                    "conditions": [
                        {
                            "column": "Analyte",
                            "value": "M2"
                        }
                    ]
                },
                "denominator": {
                    "paramcd": "AUC_all_log",
                    "conditions": [
                        {
                            "column": "Analyte",
                            "value": "Parent"
                        }
                    ]
                },
            }
        ]
    }
}
```
### 
> [!TIP]
> This same method can be used to calculate relative bioavailability for two formulations.

### Example of Custom Table with Individual and Summary Statistics
A table with selected individual PK parameters and summary statistics for those parameters is often included in a report as either an in-text or post-text table. This example code creates such a table.
```json:line-numbers
{
    "custom_tables": {
        "description": "Individual and summary PK parameter table",
        "input": {
            "source": "pk-listing.csv"
        },
        "tables": [
            {
                "layout": {
                "title": {
                    "display": true
                },
                "footer": {
                    "rows": [
                        {
                            "type": "NC",
                            "text": "**NC** = Not Calculated"
                        }
                    ],
                "display": true
                }
                },
                "stats": [
                    {
                        "name": "N",
                        "display": true
                    },
                    {
                        "name": "Mean",
                        "display": true
                    },
                    {
                        "name": "SD",
                        "display": true
                    },
                    {
                        "name": "Minimum",
                        "display": true,
                        "label": "Min"
                    },
                    {
                        "name": "Median",
                        "display": true
                    },
                    {
                        "name": "Max",
                        "display": true,
                        "label": "Max"
                    },
                    {
                        "name": "GeometricMean",
                        "display": true,
                        "label": "Geometric Mean"
                    },
                    {
                        "name": "GeometricCVP",
                        "label": "Geometric CV%"
                    }
                ],
                "file_name": "",
                "columns": [
                    {
                        "name": "subject",
                        "type": "unique_id",
                        "label": "Subject Number"
                    },
                    {
                        "name": "AUC_last_log",
                        "label": "AUC<sub>0-t</sub> <br>({{units}})",
                        "type": "statistical",
                        "sigfig": 4
                    },
                    {
                        "name": "AUC_inf_log",
                        "label": "AUC0-&infin; <br>({{units}})",
                        "type": "statistical",
                        "sigfig": 4
                    },
                    {
                        "name": "AUC_inf_log_extrap",
                        "label": "%AUC <sub>extrap</sub> <br>({{units}})",
                        "type": "statistical",
                        "sigfig": 4
                    },
                    {
                        "name": "Cmax",
                        "label": "C<sub>max</sub> <br>({{units}})",
                        "type": "statistical",
                        "sigfig": 4
                    },
                    {
                        "name": "Tmax",
                        "label": "t<sub>max</sub><br>({{units}})",
                        "type": "statistical",
                        "decimals": 2
                    },
                    {
                        "name": "kel_thalf",
                        "label": "t<sub>1/2</sub> <br>({{units}})",
                        "type": "statistical",
                        "decimals": 2
                    }
                ],
                "groups": [
                    "Cohort"
                ],
                 "styles": [
                    {
                        "border": {
                            "sides": "right",
                            "style": "solid",
                            "color": "#000000",
                            "size": "1px"
                        },
                        "columns": [
                            "subject"
                        ]
                    }
                ],
                "type": "individual_summary_pk_parameters",
                "title": "Treatment: {{TREATMENT_PLACE_Treatment}} ({{COHORT}})",
                "conditions": [
                    {
                        "column": "Cohort",
                        "value": "Cohort 1"
                    }
                ],
                "replacement_mapping": [
                    {
                        "column": "Treatment",
                        "placeholder": "{{TREATMENT_PLACE_Treatment}}"
                    },
                    {
                        "column": "Cohort",
                        "placeholder": "{{COHORT}}"
                    }
                ]
            }
        ]
    }
}
```

### Example of custom plot
Plots of concentration-time data are essential for the communication of PK results in reports and presentations. Aplos NCA allows for full customization of plots including individual and mean profiles. The following code is an example of a plot with all subjects from a single study cohort.
```json:line-numbers
{
    "custom_plots": {
        "plots": [
            {
                "title": "Individual Concentration Profiles for Cohort 1",
                "type": "all_individual_linear",
                "y_axis_column_name": "PKLEVEL2",
                "break_value": "6",
                "concentration_units_column": "Conc_units",
                "color_group_column_name": "subject",
                "reference_value": "Cohort 1",
                "x_axis_label": "Time ({{value}})",
                "color_group_label_name": "Subject Number",
                "theme": "default",
                "x_axis_column_name": "time",
                "conditions": [
                    {
                        "column": "Cohort",
                        "value": "Cohort 1"
                    }
                ],
                "time_units_column": "time_units",
                "y_axis_label": "Concentration ({{value}})"
            }
        ]
    }
}
```

### Example of Report
Creation of reports with tables and figures is also an important component of PK analysis. The following code shows the creation of a report that includes all custom plots and tables that were created in post-processing.
```json:line-numbers
{
    "custom_reports": {
        "reports": [
            {
                "template": "template_v1.docx",
                "author": "Aplos Analytics",
                "blocks": [
                    "tables",
                    "plots"
                ],
                "name": "Custom Report",
                "description": "A custom report generated by Aplos Analytics",
                "version": "1.0.0",
                "actions": [
                    "auto_update"
                ]
            }
        ]
    }
}
```

