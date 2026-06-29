# 🟠 Designations Configuration
A description of each setting on the Designations configuration screen (Figure 1) is below. All of these designations can be set globally for all profiles in the dataset, or individually for each unique profile using a data column.

|Field name|Description|
|:---|:---|
|BLQ Samples|Text designation for samples below the limit of quantitation in the Observed Concentration column. Only 1 value is accepted.|
|Missing Samples|Text designation for missing samples in the Observed Concentration column. Only 1 value is accepted.|
|Concentration unit|Text string for units associated with Analyzed Concentration column|
|Dose unit|Text string for units associated with the Dose Amount|
|Time unit|Text string for units associated with the Time column|

**Figure 1: Designation configuration input screen**
<div style="position: relative; box-sizing: content-box; max-height: 80vh; max-height: 80svh; width: 100%; aspect-ratio: 1.60; padding: 40px 0 40px 0;">
  <iframe src="https://guides.aplosanalytics.com/embed/cmqsptoo00jbdqmjazwmg38xx?embed_v=2&utm_source=embed" loading="lazy" title="PK Analysis - Designations" allow="clipboard-write" frameborder="0" webkitallowfullscreen="true" mozallowfullscreen="true" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

## 
> [!WARNING]
> The text designations for BLQ and Missing Samples require an exact match for the sample to be counted as either BLQ or Missing. Only a single text value can be used in these fields. Be aware that your results may not be as expected in the following situations:
>
> BLQ values are recorded as "BLQ (<0.10)" and "BLQ (<0.15)" because 2 different assays were used. 
> -   To properly count BLQ samples, it is recommended that you create a separate column with "BLQ" as the value.
>
> Missing samples are recorded as "NS" (no sample), "ND" (not done), or "Missing" because there are different reasons for missing samples. 
> -   To properly count Missing samples, it is recommended that you create a separate column with "Missing" as the value.
