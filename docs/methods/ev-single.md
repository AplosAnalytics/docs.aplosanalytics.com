# Extravascular Single Dose
For extravascular administration of a single dose, the following parameters are calculated as described. The extravascular route includes oral, topical, sublingual, subcutaneous, intramuscular, rectal, and any other route that is not intravenous.

## Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| AUC all linear | AUC_all_lin | Sum of partial AUC values for all time points using the [linear method](aucmethods.md) |
| AUC all linear/Dose | AUC_all_lin_D | ${AUC\_all\_lin} \over {Dose}$ |
| AUC all linlog | AUC_all_log | Sum of partial AUC values for all time points using the [linear up log down method](aucmethods.md) |
| AUC all linlog/Dose | AUC_all_log_D | ${AUC\_all\_log} \over {Dose}$ |
| AUC last linear | AUC_last_lin | Sum of partial AUC values from time of dose administration through Tlast using the [linear method](aucmethods.md) |
| AUC last linear/Dose | AUC_last_lin_D | ${AUC\_last\_lin} \over {Dose}$ |
| AUC last linlog | AUC_last_log | Sum of partial AUC values from time of dose administration through Tlast using the [linear up log down method](aucmethods.md) |
| AUC last linlog/Dose | AUC_last_log_D | ${AUC\_last\_log} \over {Dose}$ |
| AUMC all linear | AUMC_all_lin | Sum of partial AUMC values for all time points using the [linear methd](aumcmethods.md) |
| AUMC last linlog | AUMC_all_log | Sum of partial AUMC values ffor all time points using the [linear up log down methd](aumcmethods.md) |
| AUMC last linear | AUMC_last_lin | Sum of partial AUMC values from time of dose administration through Tlast using the [linear methd](aumcmethods.md) |
| AUMC last linlog | AUMC_last_log | Sum of partial AUMC values from time of dose administration through Tlast using the [linear up log down methd](aumcmethods.md) |
| Last measurable concentration | Clast | Analyzed concentration value greater than zero with the largest associated time value. |
| Maximum concentration | Cmax | Maximum concentration value in the analyzed concentration column. |
| Cmax/Dose | Cmax_D | ${Cmax} \over {Dose}$ |
| Minimum concentration | Cmin | Minimum concentration value in the analyzed concentration column. |
| Dose | Dose | Dose amount |
| Time of Dose | Dose_time | Time of dose administration |
| Number of BLQ samples | N_blq | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | N_miss | Total number of observed concentrations reported as "Missing" |
| Number of samples | N_samp | Total number of records in the observed concentration column. Observations that are below the limit of quantitation (BLQ) are counted, but missing observations are not counted. |
| Lag time | Tlag | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Time of Clast | Tlast | Value in the time column the corresponds to Clast. |
| Time of Cmax | Tmax | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Time of Cmin | Tmin | Value in time column that corresponds to the minimum concentration. If there are two identical values at the minimum concentration, the earliest time is reported. |

## Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| AUC infinity linear | AUC_inf_lin | $AUC\_last\_lin + {{Clast} \over {kel}}$ | 
| AUC infinity linear/Dose | AUC_inf_lin_D | ${AUC\_inf\_lin} \over {Dose}$ | 
| Percent extrapolated AUC infinity linear | AUC_inf_lin_extrap | $100 * [{{AUC\_inf\_lin - AUC\_last\_lin} \over {AUC\_inf\_lin}}]$ | 
| AUC infinity linlog | AUC_inf_log | $AUC\_last\_log + {{Clast} \over {kel}}$ | 
| AUC infinity linlog/Dose | AUCINFLOG_D | ${AUC\_inf\_log} \over {Dose}$ | 
| Percent extrapolated AUC infinity linlog | AUC_inf_log_extrap | $100 * [{{AUC\_inf\_log - AUC\_last\_log} \over {AUC\_inf\_log}}]$ | 
| AUMC infinity linear | AUMC_inf_lin | $AUMC\_last\_lin + {{Clast*Tlast} \over {kel}} + {{Clast} \over {kel^2}}$ | 
| Percent extrapolated AUMC infinity linear | AUMC_inf_lin_extrap |$100 * [{{AUMC\_inf\_lin - AUMC\_last\_lin} \over {AUMC\_inf\_lin}}]$ | 
| AUMC infinity linlog | AUMC_inf_log | $AUMC\_last\_log + {{Clast*Tlast} \over {kel}} + {{Clast} \over {kel^2}}$ | 
| Percent extrapolated AUMC infinity linlog | AUMC_inf_log_extrap | $100 * [{{AUMC\_inf\_log - AUMC\_last\_log} \over {AUMC\_inf\_log}}]$ | 
| CL/F linear | CL_f_lin | ${{Dose} \over {AUC\_inf\_lin}}$ | 
| CL/F linlog | CL_f_log | ${{Dose} \over {AUC\_inf\_log}}$ | 
| MRT last linear | MRT_last_lin | ${AUMC\_last\_lin} \over {AUC\_last\_lin}$ | 
| MRT last linlog | MRT_last_log | ${AUMC\_last\_log} \over {AUC\_last\_log}$ | 
| MRT linear | MRT_lin | ${AUMC\_inf\_lin} \over {AUC\_inf\_lin}$ | 
| MRT linlog | MRT_log | ${AUMC\_inf\_log} \over {AUC\_inf\_log}$ | 
| Vz/F linear | Vz_f_lin | ${{Dose} \over {kel*AUC\_inf\_lin}}$ | 
| Vz/F linlog | Vz_f_log | ${{Dose} \over {kel*AUC\_inf\_log}}$ | 
| Terminal slope group | group | Group number for each estimated terminal slope. For each profile at least one [terminal slope](terminalslope.md) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope intercept | intercept | Intercept of linear regression. | 
| Terminal slope | kel | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope adjusted r-squared | kel_adjr2 | $1 - (1 - kel\_r2)*[{{kel\_n - 1} \over {kel\_n - 2}}]$ | 
| Terminal slope lower time point | kel_low | Smallest time value used to calculate the terminal slope. | 
| Number of data points in terminal slope calculation | kel_n | Number of samples included in teh terminal slope calculation. | 
| Terminal slope r-squared | kel_r2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope span | kel_span | ${kel\_upper - kel\_low} \over {kel\_thalf}$ | 
| Terminal half life | kel_thalf | ${ln(2)} \over {kel}$ | 
| Terminal slope upper time point | kel_upper | Largest time value used to calculate the terminal slope. |
