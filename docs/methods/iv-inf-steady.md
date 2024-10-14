# 🩺🩺 IV Infusion Steady State
For IV Infusion administration at steady state, the following parameters are calculated as described. The term steady state means that the rate of input and rate of elimination of the drug are equivalent; however, there is nothing in the data of a single dosing interval that can independently determine if steady state has been achieved. A user must confirm that steady state has been achieved by other methods (e.g. monitoring trough values over several dosing intervals).

## Imputations
If the analysis dataset does not include a concentration value at the time of dose administration, a value will be imputed from the dataset. That value will be the minimum observed concentration between the time of dose administration and dose administration plus the dosing interval (Tau). The imputed concentration will be added to the dataset with a time value equal to the time of dose administration. This value is used in all parameter calculations.

If the analysis dataset does not include a concentration value at time Tau, a value will be imputed from the dataset. That value will be extrapolated from the last time point prior to Tau using the terminal elimination rate constant as described in [extrapolation methods](./extrapolationmethods).

## Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| AUC all linear | AUC_all_lin | Sum of partial AUC values for all time points using the [linear method](./aucmethods) |
| AUC all linear/Dose | AUC_all_lin_D | ${AUC_all_lin} \over {Dose}$ |
| AUC all linlog | AUC_all_log | Sum of partial AUC values for all time points using the [linear up log down method](./aucmethods) |
| AUC all linlog/Dose | AUC_all_log_D | ${AUC_all_log} \over {Dose}$ |
| AUC last linear | AUC_last_lin | Sum of partial AUC values from time of dose administration through Tlast using the [linear method](./aucmethods) |
| AUC last linear/Dose | AUC_last_lin_D | ${AUC_last_lin} \over {Dose}$ |
| AUC last linlog | AUC_last_log | Sum of partial AUC values from time of dose administration through Tlast using the [linear up log down method](./aucmethods) |
| AUC last linlog/Dose | AUC_last_log_D | ${AUC_last_log} \over {Dose}$ |
| AUMC all linear | AUMC_all_lin | Sum of partial AUMC values for all time points using the [linear methd](./aumcmethods) |
| AUMC all linlog | AUMC_all_log | Sum of partial AUMC values for all time points using the [linear up log down methd](./aumcmethods) |
| AUMC last linear | AUMC_last_lin | Sum of partial AUMC values from time of dose administration through Tlast using the [linear methd](./aumcmethods) |
| AUMC last linlog | AUMC_last_log | Sum of partial AUMC values from time of dose administration through Tlast using the [linear up log down methd](./aumcmethods) |
| Last measurable concentration | Clast | Analyzed concentration value greater than zero with the largest associated time value. |
| Maximum concentration | Cmax | Maximum concentration value in the analyzed concentration column. |
| Cmax/Dose | Cmax_D | ${Cmax} \over {Dose}$ |
| Minimum concentration | Cmin | Minimum concentration value in the analyzed concentration column. |
| Dose | Dose | Dose amount |
| Time of Dose | Dose_time | Time of dose administration |
| Duration of infusion | Inf_dur | Duration of infusion |
| End of infusion | Inf_end | End of infusion |
| Infusion rate | Inf_rate | Infusion rate |
| Start of infusion | Inf_start | Start of infusion |
| Number of BLQ samples | N_blq | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | N_miss | Total number of observed concentrations reported as "Missing" |
| Number of samples | N_samp | Total number of records in the observed concentration column. Observations that are below the limit of quantitation (BLQ) are counted, but missing observations are not counted. |
| Swing | Swing | ${(Cmax - Cmin)} \over {Cmin}$   Reported as missing if Cmin = 0. || Lag time | Tlag | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Time of Clast | Tlast | Value in the time column the corresponds to Clast. |
| Time of Cmax | Tmax | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Time of Cmin | Tmin | Value in time column that corresponds to the minimum concentration. If there are two identical values at the minimum concentration, the earliest time is reported. |
| End of dosing interaval | end_interval | Time of the end of the dosing interval |
| Tau | tau | Dosing interval |

## Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| AUC Tau linear | AUC_tau_lin | Sum of partial AUC values from time of dose administration through end_interval using the [linear method](./aucmethods) | 
| AUC Tau linear/Dose | AUC_tau_lin_D | ${AUC_tau_lin} \over {Dose}$ | 
| Percent extrapolated AUC Tau linear | AUC_tau_lin_extrap | $100 * [{{AUC_tau_lin - AUC_last_lin} \over {AUC_tau_lin}}]$; otherwise 0. | 
| AUC Tau linlog | AUC_tau_log | Sum of partial AUC values from time of dose administration through end_interval using the [linear up log down method](./aucmethods) | 
| AUC Tau linlog/Dose | AUCINFLOG_D | ${AUC_tau_log} \over {Dose}$ | 
| Percent extrapolated AUC Tau linlog | AUC_tau_log_extrap | $100 * [{{AUC_tau_log - AUC_last_log} \over {AUC_tau_log}}]$; otherwise 0. | 
| AUMC Tau linear | AUMC_tau_lin | Sum of partial AUMC values from time of dose administration through end_interval using the [linear methd](./aumcmethods) |
| AUMC Tau linlog | AUMC_tau_log | Sum of partial AUMC values from time of dose administration through end_interval using the [linear up log down methd](./aumcmethods) |
| Accumulation index | Acc_index | ${1} \over {(1 - e^{-kel * Tau})}$ |
| CLss linear | CLss_lin | ${{Dose} \over {AUC_tau_lin}}$ | 
| CLss linlog | CLss_log | ${{Dose} \over {AUC_tau_log}}$ | 
| Average concentration linear | Cavg_lin | ${AUC_tau_lin} \over {Tau}$ |
| Average concentration linlog | Cavg_log | ${AUC_tau_log} \over {Tau}$ |
| Trough concentration | Ctau | Concentration at time equal to end_interval. If an observed value is not available, [logarithmic extrapolation](./extrapolationmethods) using Clast and kel is performed. Reported as 0 if there is a BLQ value at time equal to end_interval. |
| Fluctuation linear | Fluct_lin | $100 * {{(Cmax - Cmin)} \over {Cavg_lin}}$ |
| Fluctuation linlog | Fluct_log | $100 * {{(Cmax - Cmin)} \over {Cavg_log}}$ |
| Fluctuation Tau linear | Fluct_tau_lin | $100 * {{(Cmax - Ctau)} \over {Cavg_lin}}$ |
| Fluctuation Tau linlog | Fluct_tau_log | $100 * {{(Cmax - Ctau)} \over {Cavg_log}}$ |
| MRT linear | MRT_lin | ${AUMC_tau_lin} \over {AUC_tau_lin}$ | 
| MRT linlog | MRT_log | ${AUMC_tau_log} \over {AUC_tau_log}$ | 
| Swing with Ctau | Swing_Tau | ${(Cmax - Ctau)} \over {Ctau}$   Reported as missing if Ctau = 0. |
| Vss linear | Vss_lin | $MRT_lin * CL_lin$ |
| Vss linlog | Vss_log | $MRT_log * CL_log$ |
| Vz/F linear | Vz_f_lin | ${{Dose} \over {kel*AUC_tau_lin}}$ | 
| Vz/F linlog | Vz_f_log | ${{Dose} \over {kel*AUC_tau_log}}$ | 
| Terminal slope group | group | Group number for each estimated terminal slope. For each profile at least one [terminal slope](./terminalslope) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope intercept | intercept | Intercept of linear regression. | 
| Terminal slope | kel | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope adjusted r-squared | kel_adjr2 | $1 - (1 - {kel\_r2})*[{{kel_n - 1} \over {kel_n - 2}}]$ | 
| Terminal slope lower time point | kel_low | Smallest time value used to calculate the terminal slope. | 
| Number of data points in terminal slope calculation | kel_n | Number of samples included in teh terminal slope calculation. | 
| Terminal slope r-squared | kel_r2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope span | kel_span | ${kel_upper - kel_low} \over {kel_thalf}$ | 
| Terminal half life | kel_thalf | ${ln(2)} \over {kel}$ | 
| Terminal slope upper time point | kel_upper | Largest time value used to calculate the terminal slope. |
