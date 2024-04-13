# Aplos NCA

## Introduction
Aplos NCA is a cloud-based application programming interface or API that calculates pharmacokinetic parameters from concentration-time data. These documents provide an overview of the operation of Aplos NCA, an explanation of the features and benefits, a description of the calculation methodologies employed, and instructions on how to use the API. Detailed instructions on the API endpoint and options are [documented separately](/docs/api/).

## asdf
asdf
NCA parameters are calculated for each unique pharmacokinetic profile in the analysis dataset. Unique profiles are determined by the unique combinations of the subject identifier column and all unique values of each sort variable provided in the configuration. The parameters calculated for each route of administration and dosing frequency are included in the following pages:

- [IV Bolus - single dose](IVBolusSingleDose.md)
- [IV Infusion - single dose](IVInfusionSingleDose.md)
- [Extravascular administration - single dose](ExtravascularSingleDose.md)
- [IV Bolus - steady state](IVBolusSteadyState.md)
- [IV Infusion - steady state](IVInfusionSteadyState.md)
- [Extravascular administration - steady state](ExtravascularSteadyState.md)