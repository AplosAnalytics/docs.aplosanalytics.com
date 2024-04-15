# IV Bolus Steady State
For IV Bolus at steady state, the following parameters are calculated as described. The term steady state means that the rate of input and rate of elimination of the drug are equivalent; however, there is nothing in the data of a single dosing interval that can independently determine if steady state has been achieved. A user must confirm that steady state has been achieved by other methods (e.g. monitoring trough values over several dosing intervals).

## Imputations
If the analysis dataset does not include a concentration value at the time of dose administration, a value will be imputed from the dataset. That value will be the minimum observed concentration between the time of dose administration and dose administration plus the dosing interval (Tau). The imputed concentration will be added to the dataset with a time value equal to the time of dose administration. This value is used in all parameter calculations.

If the analysis dataset does not include a concentration value at time Tau, a value will be imputed from the dataset. That value will be extrapolated from the last time point prior to Tau using the terminal elimination rate constant as described in [extrapolation methods](./extrapolationmethods).

## Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| AUC all linear C0 | AUC_all_lin_C0 | Sum of partial AUC values for all time points including C0 using the [linear method](./aucmethods) |
| AUC all linear C0/Dose | AUC_all_lin_C0_D | ${AUC\_all\_lin\_C0} \over {Dose}$ |
| AUC all linlog C0 | AUC_all_log_C0 | Sum of partial AUC values for all time points including C0 using the [linear up log down method](./aucmethods) |
| AUC all linlog C0/Dose | AUC_all_log_C0_D | ${AUC\_all\_log\_C0} \over {Dose}$ |
| AUC last linear C0 | AUC_last_lin_C0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear method](./aucmethods) |
| AUC last linear C0/Dose | AUC_last_lin_C0_D | ${AUC\_last\_lin\_C0} \over {Dose}$ |
| AUC last linlog C0 | AUC_last_log_C0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear up log down method](./aucmethods) |
| AUC last linlog C0/Dose | AUC_last_log_C0_D | ${AUC\_last\_log\_C0} \over {Dose}$ |
| AUMC last linear C0 | AUMC_last_lin_C0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear methd](./aumcmethods) |
| AUMC last linlog C0 | AUMC_last_log_C0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear up log down methd](./aumcmethods) |
| C0 | C0 | [Log-linear extrapolation](./extrapolationmethods) back to time of dose administration using the first 2 measured concentration time point. |
| Last measurable concentration | Clast | Analyzed concentration value greater than zero with the largest associated time value. |
| Maximum concentration | Cmax | Maximum concentration value in the analyzed concentration column. |
| Minimum concentration | Cmin | Minimum concentration value in the analyzed concentration column. |
| Dose | Dose | Dose amount |
| Time of Dose | Dose_time | Time of dose administration |
| MRT last linear C0 | MRT_last_lin_C0 | ${AUMC\_last\_lin\_C0} \over {AUC\_last\_lin\_C0}$ |
| MRT last linlog C0 | MRT_last_lin_C0 | ${AUMC\_last\_log\_C0} \over {AUC\_last\_log\_C0}$ |
| Number of BLQ samples | N_blq | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | N_miss | Total number of observed concentrations reported as "Missing" |
| Number of samples | N_samp | Total number of records in the observed concentration column. Observations that are 
| Swing | Swing | ${(Cmax - Cmin)} \over {Cmin}$   Reported as missing if Cmin = 0. || Lag time | Tlag | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Time of Clast | Tlast | Value in the time column the corresponds to Clast. |
| Time of Cmax | Tmax | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Time of Cmin | Tmin | Value in time column that corresponds to the minimum concentration. If there are two identical values at the minimum concentration, the earliest time is reported. |
| End of dosing interaval | end_interval | Time of the end of the dosing interval |
| Partial AUC from C0 linear | pAUC_C0_lin | Partial area under the curve from C0 to the first measured timepoint using the [linear method](./aucmethods) |
| Partial AUC from C0 linlog | pAUC_C0_log | Partial area under the cuver from C0 to the first measured timepoint using the [linear up log down methd](./aucmethods) |
| Tau | tau | Dosing interval |

## Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| Percent AUC extrapolated to C0 linear | AUC_extrap_C0_lin | $100 * [{{pAUC\_C0\_lin} \over {AUC\_inf\_lin\_C0}}]$ |
| Percent AUC extrapolated to C0 linlog | AUC_extrap_C0_log | $100 * [{{pAUC\_C0\_log} \over {AUC\_inf\_log\_C0}}]$ |
| AUC Tau linear C0 | AUC_tau_lin_C0 | Sum of partial AUC values from time of dose administration (C0) through end_interval using the [linear method](./aucmethods) | 
| AUC Tau linear C0/Dose | AUC_tau_lin_C0_D | ${AUC\_tau\_lin\_C0} \over {Dose}$ | 
| Percent extrapolated AUC Tau linear C0 | AUC_tau_lin_C0_extrap | $100 * [{{AUC\_tau\_lin\_C0 - AUC\_last\_lin\_C0} \over {AUC\_tau\_lin\_C0}}]$; otherwise 0. | 
| AUC Tau linlog C0 | AUC_tau_log_C0 | Sum of partial AUC values from time of dose administration (C0) through end_interval using the [linear up log down method](./aucmethods) | 
| AUC Tau linlog C0/Dose | AUC_tau_log_C0_D | ${AUC\_tau\_log\_C0} \over {Dose}$ | 
| Percent extrapolated AUC Tau linlog C0 | AUC_tau_log_C0_extrap | $100 * [{{AUC\_tau\_log\_C0 - AUC\_last\_log\_C0} \over {AUC\_tau\_log\_C0}}]$; otherwise 0. | 
| AUMC Tau linear C0 | AUMC_tau_lin_C0 | Sum of partial AUMC values from time of dose administration (C0) through end_interval using the [linear methd](./aumcmethods) | 
| AUMC Tau linlog C0 | AUMC_tau_log_C0 | Sum of partial AUMC values from time of dose administration (C0) through end_interval using the [linear up log down methd](./aumcmethods) | 
| Accumulation index | Acc_index | ${1} \over {(1 - e^{-kel * Tau})}$ |
| CLss linear | CLss_lin | ${{Dose} \over {AUC\_tau\_lin\_C0}}$ | 
| CLss linlog | CLss_log | ${{Dose} \over {AUC\_tau\_log\_C0}}$ | 
| Average concentration linear | Cavg_lin | ${AUC\_tau\_lin\_C0} \over {Tau}$ |
| Average concentration linlog | Cavg_log | ${AUC\_tau\_log\_C0} \over {Tau}$ |
| Trough concentration | Ctau | Concentration at time equal to end_interval. If an observed value is not available, [logarithmic extrapolation](./extrapolationmethods) using Clast and kel is performed. Reported as 0 if there is a BLQ value at time equal to end_interval. |
| Fluctuation linear | Fluct_lin | $100 * {{(Cmax - Cmin)} \over {Cavg\_lin}}$ |
| Fluctuation linlog | Fluct_log | $100 * {{(Cmax - Cmin)} \over {Cavg\_log}}$ |
| Fluctuation Tau linear | Fluct_tau_lin | $100 * {{(Cmax - Ctau)} \over {Cavg\_lin}}$ |
| Fluctuation Tau linlog | Fluct_tau_log | $100 * {{(Cmax - Ctau)} \over {Cavg\_log}}$ |
| MRT linear | MRT_lin | ${AUMC\_tau\_lin\_C0} \over {AUC\_tau\_lin\_C0}$ | 
| MRT linlog | MRT_log | ${AUMC\_tau\_log\_C0} \over {AUC\_tau\_log\_C0}$ | 
| Swing with Ctau | Swing_Tau | ${(Cmax - Ctau)} \over {Ctau}$   Reported as missing if Ctau = 0. |
| Vss linear | Vss_lin_C0 | $MRT\_lin\_C0 * CL\_lin\_C0$ |
| Vss linlog | Vss_log_C0 | $MRT\_log\_C0 * CL\_log\_C0$ |
| Vz linear | Vz_lin_C0 | ${{Dose} \over {kel*AUC\_inf\_lin\_C0}}$ | 
| Vz linlog | Vz_log_C0 | ${{Dose} \over {kel*AUC\_inf\_log\_C0}}$ | 
| Terminal slope group | group | Group number for each estimated terminal slope. For each profile at least one [terminal slope](./terminalslope) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope intercept | intercept | Intercept of linear regression. | 
| Terminal slope | kel | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope adjusted r-squared | kel_adjr2 | $1 - (1 - {kel\_r2})*[{{kel\_n - 1} \over {kel\_n - 2}}]$ | 
| Terminal slope lower time point | kel_low | Smallest time value used to calculate the terminal slope. | 
| Number of data points in terminal slope calculation | kel_n | Number of samples included in teh terminal slope calculation. | 
| Terminal slope r-squared | kel_r2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope span | kel_span | ${kel\_upper - kel\_low} \over {kel\_thalf}$ | 
| Terminal half life | kel_thalf | ${ln(2)} \over {kel}$ | 
| Terminal slope upper time point | kel_upper | Largest time value used to calculate the terminal slope. |
