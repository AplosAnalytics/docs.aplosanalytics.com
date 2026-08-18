# Plotting Series Data

Plotting series data with Aplos NCA requires understanding how data is grouped. There are 2 types of grouping variables with different names in the formatted JSONs: `seriesCategoryColumnName` and `seriesColumnName`. The following paragraphs explain how each of these is used in different plots within Aplos NCA.

## Series Column Name
The `seriesColumnName` field tells the plot which column in your data should be used to split the data into distinct series — each with its own color, line, and legend entry. Think of it as the answer to the question: "What makes one group of data points visually distinct from another?"
<br />

### How `seriesColumnName` works
When you set `seriesColumnName` to a column in your data, each unique value in that column becomes its own series on the plot. For example, if your data contains an ANALYTE column with values DrugA and DrugB, setting `seriesColumnName: "ANALYTE"` produces two series — one for each analyte — each drawn in a different color with its own legend entry.

`{ "seriesColumnName": "ANALYTE" }`

You can also specify multiple columns as a list. When you do, the plot combines the values from all listed columns into a single label (e.g. "Subject01 / Fasted"), and each unique combination becomes its own series. This is useful when you want to split data by more than one dimension at once.

`{ "seriesColumnName": ["SUBJECTALIAS", "TRTA"] }`

### Statistical plots (e.g. Mean Plots, Grouped Bar Plot)
For plots that summarize your data before drawing — such as mean concentration-time plots or mean ± SD bar charts — `seriesColumnName` plays a dual role:

 + It defines the visual series, just as in non-statistical plots: each unique value becomes its own line or bar group with its own color.

 + It also influences how the data is grouped for summarization. When the plot calculates a mean (or other statistic), it groups rows by both the x-axis column and the series column together. This ensures that the mean is computed separately for each series at each x-axis position.

In other words: the `xAxisColumnName` and `seriesColumnName` together determine the groups over which statistics are calculated. You do not need to configure this grouping separately — it is derived automatically from these two fields.

Example: On a mean concentration-time plot with `xAxisColumnName: "HOURNOMINAL"` and `seriesColumnName: "ANALYTE"`, the plot calculates the mean concentration separately for each analyte at each nominal time point, then draws one mean line per analyte.

If `seriesColumnName` is omitted on a statistical plot, the data is summarized across all rows at each x-axis value with no further grouping, producing a single series.

## Series Category Column Name
`seriesCategoryColumnName` overrides which column drives the color (or fill) of the plot elements — without changing what data is drawn or how it is grouped into series. In other words, it's purely a visual re-coloring instruction layered on top of whatever grouping already exists.

**Example:** On a mean concentration-time plot with `xAxisColumnName: "HOURNOMINAL"` and `seriesCategoryColumnName: "TRTA"`, the plot calculates the mean concentration separately for each treatment arm at each nominal time point, then draws one mean line per treatment arm, with each arm's line in a distinct color.

### Using `seriesColumnName` alongside `seriesCategoryColumnName`
For non-box-plot types, you can use both fields together:


|`seriesColumnName` set? | `seriesCategoryColumnName` set? | Result |
| :---: | :---: | :--- |
| Yes | No | Series column drives both the grouping (which line/bar) and the color. |
| No | Yes | Category column drives both the grouping and the color. |
| Yes | Yes | Series column defines the grouping (which line/bar); category column drives the color independently. |

The third case is useful when you have many series but want to colour them by a coarser grouping. For example, 30 subjects (`seriesColumnName: "SUBJECTALIAS"`) colored by 3 treatment arms (`seriesCategoryColumnName: "TRTA"`) produces 30 lines but only 3 colors, visually grouping subjects by treatment arm. The legend shows 3 entries rather than 30.
