
# Extravascular Steady State

For extravascular administration at steady state, the following parameter are calculated as described. The extravascular route includes oral, topical, sublingual, subcutaneous, intramuscular, rectal, and any other route that is not intravenous. The term steady state means that the rate of input and rate of elimination of the drug are equivalent; however, there is nothing in the data of a single dosing interval that can independently determine if steady state has been achieved. A user must confirm that steady state has been achieved by other methods (e.g. monitoring trough values over several dosing intervals).

If the analysis dataset does not include a concentration value at the time of dose administration, a value will be imputed from the dataset. That value will be the minimum observed concentration between the time of dose administration and dose administration plus the dosing interval (Tau). The imputed concentration will be added to the dataset with a time value equal to the time of dose administration. This value is used in all parameter calculations.

## List of Parameters
### Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| Number of samples | NSAMP | Total number of records in the observed concentration column. Observations that are below the limit of quantitation (BLQ) are counted, but missing observations are not counted. |
| Number of BLQ samples | NBLQ | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | NMIS | Total number of observed concentrations reported as "Missing" |
| Maximum concentration | CMAX | Maximum concentration value in the analyzed concentration column. |
| Time of CMAX | TMAX | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Dose | DOSE | Dose amount |
| Tau | TAU | Dosing interval |
| Time of dose administration | DOSE_TIME | Time of dose administration |
| End of dosing interval | END_INTERVAL | DOSE_TIME + TAU |
| Lag time | TLAG | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Cmax/Dose | CMAX_D | ${CMAX} \over {DOSE}$ |
| Last measurable concentration | CLAST | Analyzed concentration value greater than zero with the largest associated time value. |
| Time of CLAST | TLAST | Value in the time column the corresponds to CLAST. |
| Minimum concentration | CMIN | Minimum concentration value between DOSE_TIME and END_INTERVAL. Reported as 0 if there is a BLQ value. |
| Time of CMIN | TMIN | Value in time column that corresponds to the minimum concentration. If there are two identical values at the minimum concentration, the earliest time is reported. |
| Trough concentration | CTAU | Concentration at time equal to END_INTERVAL. If an observed value is not available, [logarithmic extrapolation](extrapolationmethods.md) using CLAST and KEL is performed. Reported as 0 if there is a BLQ value at time equal to END_INTERVAL. |
| Swing | SWING | ${(CMAX - CMIN)} \over {CMIN}$   Reported as missing if CMIN = 0. |
| Swing with CTAU | SWING_TAU | ${(CMAX - CTAU)} \over {CTAU}$   Reported as missing if CTAU = 0. |
| AUC all linear | AUCALLLIN | Sum of partial AUC values for all time points using the [linear method](aucmethods.md) |
| AUC last linear | AUCLASTLIN | Sum of partial AUC values from time of dose administration through TLAST using the [linear method](aucmethods.md) |
| AUC all linlog | AUCALLLOG | Sum of partial AUC values for all time points using the [linear up log down method](aucmethods.md) |
| AUC last linlog | AUCLASTLOG | Sum of partial AUC values from time of dose administration through TLAST using the [linear up log down method](aucmethods.md) |
| AUC all linear/Dose | AUCALLLIN_D | ${AUCALLLIN} \over {DOSE}$ |
| AUC last linear/Dose | AUCLASTLIN_D | ${AUCLASTLIN} \over {DOSE}$ |
| AUC all linlog/Dose | AUCALLLOG_D | ${AUCALLLOG} \over {DOSE}$ |
| AUC last linlog/Dose | AUCLASTLOG_D | ${AUCLASTLOG} \over {DOSE}$ |
| AUMC last linear | AUMCLASTLIN | Sum of partial AUMC values from time of dose administration through TLAST using the [linear methd](aumcmethods.md) |
| AUMC last linlog | AUMCLASTLOG | Sum of partial AUMC values from time of dose administration through TLAST using the [linear up log down methd](aumcmethods.md) |
| AUC Tau linear | AUCTAULIN | Sum of partial AUC values from time of dose administration through END_INTERVAL using the [linear method](aucmethods.md) |
| AUC Tau linlog | AUCTAULOG | Sum of partial AUC values from time of dose administration through END_INTERVAL using the [linear up log down method](aucmethods.md) |
| AUC Tau linear/Dose | AUCTAULIN_D |  <span v-pre>`${AUCTAULIN} \over {DOSE}$`</span> |
| AUC Tau linlog/Dose | AUCTAULog_D |  <span v-pre>`${AUCTAULOG} \over {DOSE}$`</span> |
| Percent extrapolated AUC Tau linear | AUCTAULINEX | <span v-pre>`If DOSE_TIME + TAU > TLAST then $100 * [{{AUCTAULIN - AUCLASTLIN} \over {AUCTAULIN}}]$; otherwise 0.`</span> |
| Percent extrapolated AUC Tau linlog | AUCTAULOGEX | <span v-pre>`If DOSE_TIME + TAU > TLAST then $100 * [{{AUCTAULOG - AUCLASTLOG} \over {AUCTAULOG}}]$; otherwise 0.`</span> |
| Average concentration linear | CAVGLIN | <span v-pre>`${AUCTAULIN} \over {TAU}$`</span> |
| Average concentration linlog | CAVGLOG | <span v-pre>`${AUCTAULOG} \over {TAU}$`</span> |
| Fluctuation linear | FLUCTLIN | <span v-pre>`$100 * {{(CMAX - CMIN)} \over {CAVGLIN}}$`</span> |
| Fluctuation linlog | FLUCTLOG | <span v-pre>`$100 * {{(CMAX - CMIN)} \over {CAVGLOG}}$`</span`</span>> |
| Fluctuation Tau linear | FLUCTTAULIN | <span v-pre>`$100 * {{(CMAX - CTAU)} \over {CAVGLIN}}$`</spa`</span>n> |
| Fluctuation Tau linlog | FLUCTTAULOG | <span v-pre>`$100 * {{(CMAX - CTAU)} \over {CAVGLOG}}$`</span> |
| AUMC Tau linear | AUMCLASTLIN | Sum of partial AUMC values from time of dose administration through END_INTERVAL using the [linear methd](aumcmethods.md) |
| AUMC Tau linlog | AUMCLASTLOG | Sum of partial AUMC values from time of dose administration through END_INTERVAL using the [linear up log down methd](aumcmethods.md) |
| MRT last linear | MRTLASTLIN | ${AUMCTAULIN} \over {AUCTAUTLIN}$ |
| MRT last linear | MRTLASTLIN | ${AUMCTAULIN} \over {AUCTAULIN}$ |

### Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| Terminal slope group | KEL_GROUP | Group number for each estimated terminal slope. For each profile at least one [terminal slope](terminalslope.md) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope | KEL | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope intercept | INTERCEPT | Intercept of linear regression. | 
| Terminal slope lower time point | TSLOPELOW | Smallest time value used to calculate the terminal slope. | 
| Terminal slope upper time point | TSLOPEUPP | Largest time value used to calculate the terminal slope. |
| Number of data points in terminal slope calculation | KELN | Number of samples included in teh terminal slope calculation. | 
| Terminal half life | THALF | <span v-pre>`${ln(2)} \over {KEL}$`</span> | 
| Terminal slope span | SPAN | <span v-pre>`${TSLOPEUPP - TSLOPELOW} \over {THALF}$`</span> | 
| Terminal slope r-squared | TR2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope adjusted r-squared | TAR2 |<span v-pre>`$1 - (1 - TR2)*[{{KELN - 1} \over {KELN - 2}}]$`</span> | 
| Vz/F linear | VZ_FLIN | <span v-pre>`${{DOSE} \over {KEL*AUCTAULIN}}$`</span> | 
| Vz/F linlog | VZ_FLOG |  <span v-pre>`${{DOSE} \over {KEL*AUCTAULOG}}$`</span> | 
| CLss/F linear | CL_FLIN |  <span v-pre>`${{DOSE} \over {AUCTAULIN}}$`</span> | 
| CLss/F linlog | CL_FLIN |  <span v-pre>`${{DOSE} \over {AUCTAULOG}}$`</span> | 
| Accumulation index | ACCINDEX |  <span v-pre>`${1} \over {(1 - e^{-KEL * TAU})}$`</span> |
