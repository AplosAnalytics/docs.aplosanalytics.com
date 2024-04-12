# Extravascular Single Dose

For extravascular administration of a single dose, the following parameter are calculated as described. The extravascular route includes oral, topical, sublingual, subcutaneous, intramuscular, rectal, and any other route that is not intravenous.

## List of Parameters
### Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| Number of samples | NSAMP | Total number of records in the observed concentration column. Observations that are below the limit of quantitation {BLQ} are counted, but missing observations are not counted. |
| Number of BLQ samples | NBLQ | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | NMIS | Total number of observed concentrations reported as "Missing" |
| Maximum concentration | CMAX | Maximum concentration value in the analyzed concentration column. |
| Time of CMAX | TMAX | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Dose | DOSE | Dose amount |
| Lag time | TLAG | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Cmax/Dose | CMAX_D | ${CMAX} \over {DOSE}$ |
| Last measurable concentration | CLAST | Analyzed concentration value greater than zero with the largest associated time value. |
| Time of CLAST | TLAST | Value in the time column the corresponds to CLAST. |
| AUC all linear | AUCALLLIN | Sum of partial AUC values for all time points using the [linear method]{aucmethods.md} |
| AUC last linear | AUCLASTLIN | Sum of partial AUC values from time of dose administration through TLAST using the [linear method]{aucmethods.md} |
| AUC all linlog | AUCALLLOG | Sum of partial AUC values for all time points using the [linear up log down method]{aucmethods.md} |
| AUC last linlog | AUCLASTLOG | Sum of partial AUC values from time of dose administration through TLAST using the [linear up log down method]{aucmethods.md} |
| AUC all linear/Dose | AUCALLLIN_D | ${AUCALLLIN} \over {DOSE}$ |
| AUC last linear/Dose | AUCLASTLIN_D | ${AUCLASTLIN} \over {DOSE}$ |
| AUC all linlog/Dose | AUCALLLOG_D | ${AUCALLLOG} \over {DOSE}$ |
| AUC last linlog/Dose | AUCLASTLOG_D | ${AUCLASTLOG} \over {DOSE}$ |
| AUMC last linear | AUMCLASTLIN | Sum of partial AUMC values from time of dose administration through TLAST using the [linear methd]{aumcmethods.md} |
| AUMC last linlog | AUMCLASTLOG | Sum of partial AUMC values from time of dose administration through TLAST using the [linear up log down methd]{aumcmethods.md} |
| MRT last linear | MRTLASTLIN | ${AUMCLASTLIN} \over {AUCLASTLIN}$ |
| MRT last linear | MRTLASTLIN | ${AUMCLASTLIN} \over {AUCLASTLIN}$ |

### Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| Terminal slope group | KEL_GROUP | Group number for each estimated terminal slope. For each profile at least one [terminal slope]{terminalslope.md} is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope | KEL | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope intercept | INTERCEPT | Intercept of linear regression. | 
| Terminal slope lower time point | TSLOPELOW | Smallest time value used to calculate the terminal slope. | 
| Terminal slope upper time point | TSLOPEUPP | Largest time value used to calculate the terminal slope. |
| Number of data points in terminal slope calculation | KELN | Number of samples included in teh terminal slope calculation. | 
| Terminal half life | THALF | <span v-pre>`${ln{2}} \over {KEL}$`</span> | 
| Terminal slope span | SPAN | <span v-pre>`${TSLOPEUPP - TSLOPELOW} \over {THALF}$`</span> |
| Terminal slope r-squared | TR2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope adjusted r-squared | TAR2 | <span v-pre>`1 - {1 - TR2}*[{{KELN - 1} \over {KELN - 2}]`</span> | 
| AUC infinity linear | AUCINFLIN | <span v-pre>`AUCLASTLIN + {{CLAST} \over {KEL}`</span> | 
| Percent extrapolated AUC infinity linear | AUCLINEXT | <span v-pre>`100 * [{{AUCINFLIN - AUCLASTLIN} \over {AUCINFLIN}]`</span> | 
| AUC infinity linlog | AUCINFLOG | <span v-pre>`AUCLASTLOG + {{CLAST} \over {KEL}`</span> | 
| Percent extrapolated AUC infinity linlog | AUCLOGEXT | <span v-pre>`100 * [{{AUCINFLOG - AUCLASTLOG} \over {AUCINFLOG}]`</span> | 
| AUC infinity linear/Dose | AUCINFLIN_D | <span v-pre>`{AUCINFLIN} \over {DOSE}`</span> | 
| AUC infinity linlog/Dose | AUCINFLOG_D | <span v-pre>`{AUCINFLOG} \over {DOSE}`</span> | 
| Vz/F linear | VZ_FLIN | <span v-pre>`{{DOSE} \over {KEL*AUCINFLIN}`</span> | 
| Vz/F linlog | VZ_FLOG | <span v-pre>`{{DOSE} \over {KEL*AUCINFLOG}`</span> | 
| CL/F linear | CL_FLIN | <span v-pre>`{{DOSE} \over {AUCINFLIN}`</span> | 
| CL/F linlog | CL_FLOG | <span v-pre>`{{DOSE} \over {AUCINFLOG}`</span> | 
| AUMC infinity linear | AUMCINFLIN | <span v-pre>`AUMCLASTLIN + {{CLAST*TLAST} \over {KEL} + {{CLAST} \over {KEL^2}`</span> | 
| Percent extrapolated AUMC infinity linear | <span v-pre>`100 * [{{AUMCINFLIN - AUMCLASTLIN} \over {AUMCINFLIN}]`</span> | 
| AUMC infinity linlog | AUMCINFLOG | <span v-pre>`AUMCLASTLOG + {{CLAST*TLAST} \over {KEL} + {{CLAST} \over {KELE^2}`</span> | 
| Percent extrapolated AUMC infinity linlog | <span v-pre>`100 * [{{AUMCINFLOG - AUMCLASTLOG} \over {AUMCINFLOG}]`</span> | 
| MRT linear | MRTINFLIN | <span v-pre>`{AUMCINFLIN} \over {AUCINFLIN}`</span> | 
| MRT linlog | MRTINFLOG | <span v-pre>`{AUMCINFLOG} \over {AUCINFLOG}`</span> |