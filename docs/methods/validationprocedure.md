# 📝 Validation Procedure

Aplos NCA includes a user-initiated validation procedure to confirm the accuracy of all calculations performed by the software. The validation procedure is performed within the user's environment using the same methods and engines available to the user for standard analyses. The validation procedure performs the following actions:

1. Simultaneously execute 6 separate NCA analyses using puclicly available datasets and configurations. These are considered the "test cases".
2. Comparison of all calculated parameters versus known results and identification of any discrepancies.
3. Preparation of report with pass/fail results for each of the 6 test cases.

The test cases can be found on the public repository https://github.com/aplosanalytics/validation. A description of the 6 tests cases are:

+ Test 1: Single extravascular dose
+ Test 2: Single intravenous (IV) bolus dose
+ Test 3: Single IV infusion dose
+ Test 4: Steady-state extravascular dose
+ Test 5: Steady-state IV bolus dose
+ Test 6: Steady-state IV infusion dose 

For each test case there are 3 distinct files: (1) Input data file, (2) Configuration file, and (3) Expected output file.

### Input data file
This file includes the concentration time dataset used for the calculation of the NCA parameters
### Configuration file
This file includes the Aplos NCA configuration setttings for the analysis. It is provided as a formatted JSON structured file compatible for analysis with Aplos NCA. This structure is human readable.
### Known output
This file includes the expected NCA parameters from the analysis of the data given the configuration settings. These results have been verified by manual calculation using R and spot checked against other commercially available software packages. These results are considered to be accurate; however, users are free to analyze the input data file and compare their results to the known results for confirmation.


 

