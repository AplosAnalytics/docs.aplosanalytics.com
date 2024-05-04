# Summary PK Parameters
The results include a sumamry of all calculated PK parameters. The results are provided in both HMTL and CSV formats.

## Summary statistics
The following summary statistics are calculated for each parameter:

   -   Mean 
   -   Standard deviation
   -   Coefficient of variation
   -   Median
   -   Minimum
   -   Maximum
   -   Geometric mean
   -   Geometric coefficient of variation
   -   Number of values
   -   Number of missing values

## HTML results
The HTML results include a table with two columns. The first column is the parameter name along with the summary statistics. The second column contains the calculated summary statistics for each parameter.

## CSV results
The CSV results include 3 columns of data. The first column is the PK parameter name, the second column is the summary statistic variable name, and the third column is the value for the summary statistic variable for that PK parameter.

## Grouping variables
When grouping variable(s) are included in the analysis, multiple summaries are produced. A summary is produced for each unique value of a grouping variable, and any combinations if there are multiple grouping variables. The examples below illustrate the summaries that are provided for a few common scenarios.
> [!TIP] Example with Sex as grouping variable
> Grouping variable: Sex
> Unique values of grouping variable: Female, Male
> Summaries provided:
>    -   All subject profiles
>    -   Female subject profiles
>    -   Male subject profiles

An a slightly more complex example: 

> [!TIP] Example with Sex and Dose as grouping variables
> Grouping variable 1: Sex
> Unique values of grouping variable: Female, Male
> Grouping variable 2: Dose
> Unique values of grouping variable: 5, 10, 20, 50
> Summaries provided:
>    -   All subject profiles
>    -   Female subject profiles
>    -   Male subject profiles
>    -   Dose = 5 subject profiles
>    -   Dose = 10 subject profiles
>    -   Dose = 20 subject profiles
>    -   Dose = 50 subject profiles
>    -   Female Dose = 5 subject profiles
>    -   Female Dose = 10 subject profiles
>    -   Female Dose = 20 subject profiles
>    -   Female Dose = 50 subject profiles
>    -   Male Dose = 5 subject profiles
>    -   Male Dose = 10 subject profiles
>    -   Male Dose = 20 subject profiles
>    -   Male Dose = 50 subject profiles

And a really complex example:

> [!TIP] Example with Sex, Dose and Formulation grouping variables
> Grouping variable 1: Sex
> Unique values of grouping variable: Female, Male
> Grouping variable 2: Dose
> Unique values of grouping variable: 5, 10
> Grouping variable 2: Formulation
> Unique values of grouping variable: Capsule, Tablet
> Summaries provided:
>    -   All subject profiles
>    -   Female subject profiles
>    -   Male subject profiles
>    -   Dose = 5 subject profiles
>    -   Dose = 10 subject profiles
>    -   Capsule subject profiles
>    -   Tablet subject profiles
>    -   Female Dose = 5 subject profiles
>    -   Female Dose = 10 subject profiles
>    -   Female Capsule subject profiles
>    -   Female Tablet subject profiles
>    -   Male Dose = 5 subject profiles
>    -   Male Dose = 10 subject profiles
>    -   Male Capsule subject profiles
>    -   Male Tablet subject profiles
>    -   Female Dose = 5 Capsule subject profiles
>    -   Female Dose = 5 Tablet subject profiles
>    -   Female Dose = 10 Capsule subject profiles
>    -   Female Dose = 10 Tablet subject profiles
>    -   Male Dose = 5 Capsule subject profiles
>    -   Male Dose = 5 Tablet subject profiles
>    -   Male Dose = 10 Capsule subject profiles
>    -   Male Dose = 10 Tablet subject profiles

