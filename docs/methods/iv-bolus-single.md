# IV Bolus Single Dose
For IV Bolus administration of a single dose, the following parameters are calculated as described. 

## Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| AUC all linear C0 | AUC_all_lin_C0 | Sum of partial AUC values for all time points including C0 using the [linear method](aucmethods.md) |
| AUC all linear C0/Dose | AUC_all_lin_C0_D | ${AUC\_all\_lin\_C0} \over {Dose}$ |
| AUC all linlog C0 | AUC_all_log_C0 | Sum of partial AUC values for all time points including C0 using the [linear up log down method](aucmethods.md) |
| AUC all linlog C0/Dose | AUC_all_log_C0_D | ${AUC\_all\_log\_C0} \over {Dose}$ |
| AUC last linear C0 | AUC_last_lin_C0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear method](aucmethods.md) |
| AUC last linear C0/Dose | AUC_last_lin_C0_D | ${AUC\_last\_lin\_C0} \over {Dose}$ |
| AUC last linlog C0 | AUC_last_log_C0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear up log down method](aucmethods.md) |
| AUC last linlog C0/Dose | AUC_last_log_C0_D | ${AUC\_last\_log\_C0} \over {Dose}$ |
| AUMC last linear C0 | AUMC_last_lin_C0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear methd](aumcmethods.md) |
| AUMC last linlog C0 | AUMC_last_log_C0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear up log down methd](aumcmethods.md) |
| C0 | C0 | [Log-linear extrapolation](extrapolationmethods.md) back to time of dose administration using the first 2 measured concentration time point. |
| Last measurable concentration | Clast | Analyzed concentration value greater than zero with the largest associated time value. |
| Dose | Dose | Dose amount |
| MRT last linear C0 | MRT_last_lin_C0 | ${AUMC\_last\_lin\_C0} \over {AUC\_last\_lin\_C0}$ |
| MRT last linlog C0 | MRT_last_lin_C0 | ${AUMC\_last\_log\_C0} \over {AUC\_last\_log\_C0}$ |
| Number of BLQ samples | N_blq | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | N_miss | Total number of observed concentrations reported as "Missing" |
| Number of samples | N_samp | Total number of records in the observed concentration column. Observations that are 
| Time of Clast | Tlast | Value in the time column the corresponds to Clast. |
| Partial AUC from C0 linear | pAUC_C0_lin | Partial area under the curve from C0 to the first measured timepoint using the [linear method](aucmethods.md) |
| Partial AUC from C0 linlog | pAUC_C0_log | Partial area under the cuver from C0 to the first measured timepoint using the [linear up log down methd](aucmethods.md) |

## Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| Percent AUC extrapolated to C0 linear | AUC_extrap_C0_lin | $100 * [{{pAUC\_C0\_lin} \over {AUC\_inf\_lin\_C0}}]$ |
| Percent AUC extrapolated to C0 linlog | AUC_extrap_C0_log | $100 * [{{pAUC\_C0\_log} \over {AUC\_inf\_log\_C0}}]$ |
| AUC infinity linear C0 | AUC_inf_lin_C0 | $AUC\_last\_lin\_C0 + {{Clast} \over {kel}}$ | 
| AUC infinity linear C0/Dose | AUC_inf_lin_C0_D | ${AUC\_inf\_lin\_C0} \over {Dose}$ | 
| Percent extrapolated AUC infinity linear C0 | AUC_inf_lin_C0_extrap | $100 * [{{AUC\_inf\_lin\_C0 - AUC\_last\_lin\_C0} \over {AUC\_inf\_lin\_C0}}]$ | 
| AUC infinity linlog C0 | AUC_inf_log_C0 | $AUC\_last\_log\_C0 + {{Clast} \over {kel}}$ | 
| AUC infinity linlog C0/Dose | AUC\_inf\_log\_C0\_D | ${AUC\_inf\_log\_C0} \over {Dose}$ | 
| Percent extrapolated AUC infinity linlog C0 | AUC_inf_log_C0_extrap | $100 * [{{AUC\_inf\_lin\_C0 - AUC\_last\_log\_C0} \over {AUC\_inf\_lin\_C0}}]$ | 
| AUMC infinity linear C0 | AUMC_inf_lin_C0 | $AUMC\_last\_lin\_C0 + {{Clast*Tlast} \over {kel}} + {{Clast} \over {kel^2}}$ | 
| Percent extrapolated AUMC infinity linear C0 | AUMC_inf_lin_C0_extrap | $100 * [{{AUMC\_inf\_lin\_C0 - AUMC\_last\_lin\_C0} \over {AUMC\_inf\_lin\_C0}}]$ | 
| AUMC infinity linlog | AUMC_inf_log_C0 | $AUMC\_last\_log\_C0 + {{Clast*Tlast} \over {kel}} + {{Clast} \over {kel^2}}$ | 
| Percent extrapolated AUMC infinity linlog C0 | AUMC_inf_log_C0_extrap | $100 * [{{AUMC\_inf\_log\_C0 - AUMC\_last\_log\_C0} \over {AUMC\_inf\_log\_C0}}]$ | 
| CL linear | CL_lin_C0 | ${{Dose} \over {AUC\_inf\_lin\_C0}}$ | 
| CL linlog | CL_log_C0 | ${{Dose} \over {AUC\_inf\_log\_C0}}$ | 
| MRT last linear | MRT_last_lin_C0 | ${AUMC\_last\_lin\_C0} \over {AUC\_last\_lin\_C0}$ | 
| MRT last linlog | MRT_last_log_C0 | ${AUMC\_last\_log\_C0} \over {AUC\_last\_log\_C0}$ | 
| MRT linear | MRT_lin_C0 | ${AUMC\_inf\_lin\_C0} \over {AUC\_inf\_lin\_C0}$ | 
| MRT linlog | MRT_log_C0 | ${AUMC\_inf\_log\_C0} \over {AUC\_inf\_log\_C0}$ | 
| Vss linear | Vss_lin_C0 | $MRT\_lin\_C0 * CL\_lin\_C0$ |
| Vss linlog | Vss_log_C0 | $MRT\_log\_C0 * CL\_log\_C0$ |
| Vz linear | Vz_lin_C0 | ${{Dose} \over {kel*AUC\_inf\_lin\_C0}}$ | 
| Vz linlog | Vz_log_C0 | ${{Dose} \over {kel*AUC\_inf\_log\_C0}}$ | 
| Terminal slope group | group | Group number for each estimated terminal slope. For each profile at least one [terminal slope](terminalslope.md) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope intercept | intercept | Intercept of linear regression. | 
| Terminal slope | kel | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope adjusted r-squared | kel_adjr2 | $1 - (1 - {kel\_r2})*[{{kel\_n - 1} \over {kel\_n - 2}}]$ | 
| Terminal slope lower time point | kel_low | Smallest time value used to calculate the terminal slope. | 
| Number of data points in terminal slope calculation | kel_n | Number of samples included in teh terminal slope calculation. | 
| Terminal slope r-squared | kel_r2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope span | kel_span | ${kel\_upper - kel\_low} \over {kel\_thalf}$ | 
| Terminal half life | kel_thalf | ${ln(2)} \over {kel}$ | 
| Terminal slope upper time point | kel_upper | Largest time value used to calculate the terminal slope. |
