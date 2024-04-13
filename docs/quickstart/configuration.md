# Configure Analysis Settings
The configuration screen includes 6 separate sections. The first 4 sections require information about the analysis dataset. The last 2 sections are optional.

## Dosing
Enter information about the dose administration in this section. The following table includes an explanation of each entry item and the value required for the sample dataset. 
(screenshot of input fields)
|**Field**|**Value**|**Description**|
|:---|:---|:---|
|Frequency|Single Dose|Options are Single Dose or Steady State|
|Route|Extravascular|Options are Extravascular, IV Bolus, or IV Infusion|
|Amount|10000|Amount of dose|
|Time of Administration|0|Time dose was administered|

## Data Columns
Enter the column names from the sample dataset associated with each of the fields shown in the image below. 
(screenshot of input fields)

## Designations
Enter the information about the units, and text designations for BLQ and missing samples as shown in the image below.
(screenshot of input fields)

## Kel Rules
The Kel rules are the criteria used to select the "best-fit" terminal elimination rate constant. In this example, we will use the maximum adjusted r<sup>2</sup> as the only criterion. Enter the information as shown in the image below.
(screenshot of kel rules)

## Meta Data
Meta data is information that will be associated with the analysis within the Aplos NCA system. You can search for the meta data to locate analysis results after completion. Meta data include 2 parts: a (1) key and a (2) value. Enter the following key:value pairs as shown below.
```json
"project":"Quick start",
"compound":"AZ-123",
"study":"CL-123-001"
```

## Configuration
The configuration section shows the formatted configuration json file used for the analysis. Click the Execute button to start the analysis.
