# IV Bolus Single Dose

For IV Bolus administration of a single dose, the following parameter are calculated as described. 

## List of Parameters
### Parameters that do not depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation |
| :--- | :---: | :--- |
| Number of samples | NSAMP | Total number of records in the observed concentration column. Observations that are below the limit of quantitation (BLQ) are counted, but missing observations are not counted. |
| Number of BLQ samples | NBLQ | Total number of observed concentrations reported as "BLQ" |
| Number of missing samples | NMIS | Total number of observed concentrations reported as "Missing" |
| C0 | C0 | [Log-linear extrapolation](extrapolationmethods.md) back to time of dose administration using the first 2 measured concentration time point. |
| Maximum concentration | CMAX | Maximum concentration value in the analyzed concentration column. |
| Time of CMAX | TMAX | Value in time column that corresponds to the maximum concentration. If there are two identical values at the maximum concentration, the earliest time is reported. |
| Dose | DOSE | Dose amount |
| Lag time | TLAG | Value in time column that corresponds to the last concentration with a value of 0 after the dose administration time but before the first analyzed concentration value greater than zero. |
| Cmax/Dose | CMAX_D | ${CMAX} \over {DOSE}$ |
| Last measurable concentration | CLAST | Analyzed concentration value greater than zero with the largest associated time value. |
| Time of CLAST | TLAST | Value in the time column the corresponds to CLAST. |
| Partial AUC from C0 linear | pAUCC0LIN | Partial area under the cuver from C0 to the first measured timepoint using the [linear methd](aumcmethods.md) |
| Partial AUC from C0 linlog | pAUCC0LOG | Partial area under the cuver from C0 to the first measured timepoint using the [linear up log down methd](aumcmethods.md) |
| AUC all linear C0 | AUCALLLINC0 | Sum of partial AUC values for all time points including C0 using the [linear method](aucmethods.md) |
| AUC last linear C0 | AUCLASTLINC0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear method](aucmethods.md) |
| AUC all linlog C0 | AUCALLLOGC0 | Sum of partial AUC values for all time points including C0 using the [linear up log down method](aucmethods.md) |
| AUC last linlog C0 | AUCLASTLOGC0 | Sum of partial AUC values from time of dose administration (C0) through TLAST using the [linear up log down method](aucmethods.md) |
| AUC all linear C0/Dose | AUCALLLINC0_D | ${AUCALLLINC0} \over {DOSE}$ |
| AUC last linear C0/Dose | AUCLASTLINC0_D | ${AUCLASTLINC0} \over {DOSE}$ |
| AUC all linlog C0/Dose | AUCALLLOGC0_D | ${AUCALLLOGC0} \over {DOSE}$ |
| AUC last linlog C0/Dose | AUCLASTLOGC0_D | ${AUCLASTLOGC0} \over {DOSE}$ |
| AUMC last linear C0 | AUMCLASTLINC0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear methd](aumcmethods.md) |
| AUMC last linlog C0 | AUMCLASTLOGC0 | Sum of partial AUMC values from time of dose administration (C0) through TLAST using the [linear up log down methd](aumcmethods.md) |
| MRT last linear | MRTLASTLIN | ${AUMCLASTLINC0} \over {AUCLASTLINC0}$ |
| MRT last linear | MRTLASTLIN | ${AUMCLASTLINC0} \over {AUCLASTLINC0}$ |

### Parameters that depend on a terminal slope
| Parameter name | Parameter code in output | Description of calculation | 
| :--- | :---: | :--- |
| Terminal slope group | KEL_GROUP | Group number for each estimated terminal slope. For each profile at least one [terminal slope](terminalslope.md) is calculated. All parameters that are dependent on estimation of the terminal slope are also calcualted and given the same group number. |
| Terminal slope | KEL | Negative of estimated slope by linear regression of the natural log-transformed analyzed concentrations and the time of each observation. |
| Terminal slope intercept | INTERCEPT | Intercept of linear regression. | 
| Terminal slope lower time point | TSLOPELOW | Smallest time value used to calculate the terminal slope. | 
| Terminal slope upper time point | TSLOPEUPP | Largest time value used to calculate the terminal slope. |
| Number of data points in terminal slope calculation | KELN | Number of samples included in teh terminal slope calculation. | 
| Terminal half life | THALF | ${ln(2)} \over {KEL}$ | 
| Terminal slope span | SPAN | ${TSLOPEUPP - TSLOPELOW} \over {THALF}$ | 
| Terminal slope r-squared | TR2 | r<sup>2</sup> value from terminal slope linear regression. | 
| Terminal slope adjusted r-squared | TAR2 | $1 - (1 - TR2)*[{{KELN - 1} \over {KELN - 2}}]$ | 
| Percent AUC extrapolated to C0 linear | AUCEXTCOLIN | $100 * [{{pAUCC0LIN} \over {AUCINFLINC0}}]
| Percent AUC extrapolated to C0 linlog | AUCEXTCOLOG | $100 * [{{pAUCC0LOG} \over {AUCINFLOGC0}}]
| AUC infinity linear C0 | AUCINFLINC0 | $AUCLASTLINC0 + {{CLAST} \over {KEL}}$ | 
| Percent extrapolated AUC infinity linear C0 | AUCLINEXTC0 | $100 * [{{AUCINFLINC0 - AUCLASTLINC0} \over {AUCINFLINC0}}]$ | 
| AUC infinity linlog C0 | AUCINFLOGC0 | $AUCLASTLOGC0 + {{CLAST} \over {KEL}}$ | 
| Percent extrapolated AUC infinity linlog C0 | AUCLOGEXTC0 | $100 * [{{AUCINFLOGC0 - AUCLASTLOGC0} \over {AUCINFLOGC0}}]$ | 
| AUC infinity linear C0/Dose | AUCINFLINC0_D | ${AUCINFLINC0} \over {DOSE}$ | 
| AUC infinity linlog C0/Dose | AUCINFLOGC0_D | ${AUCINFLOGC0} \over {DOSE}$ | 
| Vz linear | VZLIN | ${{DOSE} \over {KEL*AUCINFLINC0}}$ | 
| Vz linlog | VZLOG | ${{DOSE} \over {KEL*AUCINFLOGC0}}$ | 
| CL linear | CLLIN | ${{DOSE} \over {AUCINFLINC0}}$ | 
| CL linlog | CLLOG | ${{DOSE} \over {AUCINFLOGC0}}$ | 
| Vss linear | VSSLIN | $MRTINFLIN * CLLIN$ |
| Vss linlog | VSSLOG | $MRTINFLOG * CLLOG$ |
| AUMC infinity linear C0 | AUMCINFLINC0 | $AUMCLASTLINC0 + {{CLAST*TLAST} \over {KEL}} + {{CLAST} \over {KEL^2}}$ | 
| Percent extrapolated AUMC infinity linear C0 | AUMCEXTLINC0 | $100 * [{{AUMCINFLINC0 - AUMCLASTLINC0} \over {AUMCINFLINC0}}]$ | 
| AUMC infinity linlog | AUMCINFLOG C0 | $AUMCLASTLOGC0 + {{CLAST*TLAST} \over {KEL}} + {{CLAST} \over {KELE^2}}$ | 
| Percent extrapolated AUMC infinity linlog C0 | AUMCEXTLOGC0 | $100 * [{{AUMCINFLOGC0 - AUMCLASTLOGC0} \over {AUMCINFLOGC0}}]$ | 
| MRT linear | MRTINFLIN | ${AUMCINFLINC0} \over {AUCINFLINC0}$ | 
| MRT linlog | MRTINFLOG | ${AUMCINFLOGC0} \over {AUCINFLOGC0}$ | 

