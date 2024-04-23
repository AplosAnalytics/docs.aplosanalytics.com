# Technical Report
The technical report is a compilation of all of the results and is intended to serve as an appendix to a written report by the analyst. The report is generated based on the results of the analysis performed and does not include any post-processing activities. It only describes the estimation of the PK parameters using NCA methods. The sections and content of the technical report are described below.

## Analysis Information
The first section of the technical report includes detailed information about the analysis performed including: name of analyst, unique analysis identifier, time and date of analysis, version of the API and calculation engine, and name of input dataset. All of this information uniquely identifies the analysis results.

## Analysis Configuration
The second section includes the configuration information used for the analysis. This converts the settings from the configuration json structure to a table that is easily interpreted. This can be used to confirm that the analysis was conducted as planned.

## Meta data
The third section includes the meta data submitted with the analysis. This converts all of the user-provided meta information into a table.

## Summary Plots and Tables
The [summary plots](./results-summary-plot) and [summary tables](./results-summary) generated during the analysis are included in the document.

## Individual Plots and Tables
The [individual plots](./results-ind-plot) and [individual pk parameters](./results-ind) generated during the analysis are included in the document.

## Additional thoughts
In many cases, additional post-hoc analyses may be required to calculate things such as relative bioavailability, dose proportionality, or other key aspects of the pharmacokinetics of the drug. These analyses are based on the calculated PK parameters from the NCA methods. Thus, the technical report is designed to only represent the calculation of the PK parameters. As such, this report should be considered a component of the full report for the study. In some cases, (e.g. toxicokinetic reports), this may serve as all or nearly all of the information needed in the final report. 
