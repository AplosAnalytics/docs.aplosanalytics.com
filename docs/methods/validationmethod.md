# 🟩 Validation

<span style="color:red;display:block;text-align:left;font-size: 40px;"> **COMING SOON**</span>

Validation is the process through which you can demonstrate that the PK parameters calculated using Aplos NCA are accurate. Aplos NCA includes a simple validation module to assist you in developing the evidence required to confirm that the PK parameters are accurate when you submit data for analysis. This module can become part of your overall system validation effort that aligns with your company-specific procedures.

Validation runs do not count against your annual subscription allocation. You can run the validation test at any time. Each validation result is stored and can be downloaded at a later date if needed. 

## What the validation module does

The validation module will do the following with six different input datasets:

1. Download a known input dataset from a public location
2. Analyze the input dataset using Aplos NCA
3. Download the known PK parameters from a public location
4. Compare the calculated PK parameters with the known PK parameters
5. Report on any differences

## Threshold for differences

When comparing the calculated results to the known results, a threshold of 0.01% is used to identify any meaningful differences. If the calculated result differs by more than 0.01% from the known result, then the calculated parameter is considered different from the known result.

## Criteria for Pass

If all calculated parameters are within 0.01% of the known parameters, the test result is a pass. If any single parameter is considered different from the known result, then that test is considered a fail. If all 6 test cases pass, then the validation is an overall pass. If any 1 of the test cases fails, then the validation is an overall fail.

## Test cases

The test cases are available on the [public github repository](https://github.com/AplosAnalytics/validation.git). For each test case there are 3 files: (1) input data file, (2) analysis configuration file, and (3) known results file. These files are publicly available and can be analyzed using other software packages if desired. The six specific test cases are:

|**Test**|**Route**|**Frequency**|**Files**|
|:---|:---|:---|:---|
|1|Extravascular|Single dose|**Input data:** test1_data_single_ev.csv<br>**Configuration:** test1_config_single_ev.json<br>**Known results:** test1_pk-results_single_ev.csv|
|2|IV Bolus|Single dose|**Input data:** test2_data_single_iv_bolus.csv <br>**Configuration:** test2_config_single_iv_bolus.json <br>**Known results:** test2_pk-results_single_iv_bolus.csv|
|3|IV Infusion|Single dose|**Input data:** test3_data_single_iv_infusion.csv <br>**Configuration:** test3_config_single_iv_infusion.json <br>**Known results:** test3_pk-results_single_iv_infusion.csv|
|4|Extravascular|Steady state|**Input data:** test4_data_ss_ev.csv <br>**Configuration:** test4_config_ss_ev.json <br>**Known results:** test4_pk-results_ss_ev.csv|
|5|IV Bolus|Steady state|**Input data:** test5_data_ss_iv_bolus.csv <br>**Configuration:** tes5_config_ss_iv_bolus.json <br>**Known results:** test5_pk-results_ss_iv_bolus.csv|
|6|IV Infusion|Steady state|**Input data:** test6_data_ss_iv_infusion.csv <br>**Configuration:** test6_config_ss_iv_infusion.json <br>**Known results:** test6_pk-results_ss_iv_infusion.csv|

## Results

The validation results include the Aplos NCA output for all 6 test cases plus a report that summarizes the validation test results including an overall assessment of pass or fail. The validation results can be downloaded at any time.