# ♻️ Parameter Decode List
PK parameter names can differ between software packages. This page lists the parameter names used by Aplos NCA along with the recommended CDISC parameter name and the parameter codes used in Phoenix WinNonlin. There are cases where multiple parameters from Aplos NCA match up to the same parameter names in CDISC and other software packages. This occurs because the AUC calculation method is included in the parameter name for Aplos NCA, but it is not included for CDISC or other software packages.

| Parameter name | Aplos NCA parameter code | CDISC parameter code | WinNonlin parameter code |
| :--- | :---: | :--- | :--- |
| Accumulation index | Acc_index | None | Accumulation Index |
| AUC all linear | AUC_all_lin | AUCALL | AUCall |
| AUC all linear C0 | AUC_all_lin_C0 | AUCALL | AUCall |
| AUC all linear/Dose | AUC_all_lin_D | AUCALLD | AUCall_D |
| AUC all linear C0/Dose | AUC_all_lin_C0_D | AUCALLD | AUCall_D |
| AUC all linlog | AUC_all_log | AUCALL | AUCall |
| AUC all linlog C0 | AUC_all_log_C0 | AUCALL | AUCall |
| AUC all linlog/Dose | AUC_all_log_D | AUCALLD | AUCall_D |
| AUC all linlog C0/Dose | AUC_all_log_C0_D | AUCALLD | AUCall_D |
| AUC infinity linear | AUC_inf_lin | AUCIFO | AUC_inf_obs |
| AUC infinity linear C0 | AUC_inf_lin_C0 | AUCIFO | AUC_inf_obs |
| AUC infinity linear/Dose | AUC_inf_lin_D | AUCIFOD | AUC_inf_obs_D | 
| AUC infinity linear C0/Dose | AUC_inf_lin_C0_D | AUCIFOD | AUC_inf_obs_D | 
| AUC infinity linlog | AUC_inf_log | AUCIFO | AUC_inf_obs | 
| AUC infinity linlog C0 | AUC_inf_log_C0 | AUCIFO | AUC_inf_obs | 
| AUC infinity linlog/Dose | AUCINFLOG_D | AUCIFOD | AUC_inf_obs_D | 
| AUC infinity linlog C0/Dose | AUC\_inf\_log\_C0\_D | AUCIFOD | AUC_inf_obs_D | 
| AUC last linear | AUC_last_lin | AUCLST | AUClast |
| AUC last linear C0 | AUC_last_lin_C0 | AUCLST | AUClast |
| AUC last linear/Dose | AUC_last_lin_D | AUCLSTD | AUClast_D |
| AUC last linear C0/Dose | AUC_last_lin_C0_D | AUCLSTD | AUClast_D |
| AUC last linlog | AUC_last_log | AUCLST | AUClast |
| AUC last linlog C0 | AUC_last_log_C0 | AUCLST | AUClast |
| AUC last linlog/Dose | AUC_last_log_D | AUCLSTD | AUClast_D |
| AUC last linlog C0/Dose | AUC_last_log_C0_D | AUCLSTD | AUClast_D |
| AUC Tau linear | AUC_tau_lin | AUCTAU | AUC_TAU |
| AUC Tau linear C0 | AUC_tau_lin_C0 | AUCTAU | AUC_TAU | 
| AUC Tau linear/Dose | AUC_tau_lin_D | AUCTAUD | AUC_TAU_D | 
| AUC Tau linear C0/Dose | AUC_tau_lin_C0_D | AUCTAUD | AUC_TAU_D | 
| AUC Tau linlog | AUC_tau_log | AUCTAU | AUC_TAU | 
| AUC Tau linlog C0 | AUC_tau_log_C0 | AUCTAU | AUC_TAU | 
| AUC Tau linlog/Dose | AUCINFLOG_D | AUCTAUD | AUC_TAU_D | 
| AUC Tau linlog C0/Dose | AUC_tau_log_C0_D | AUCTAUD | AUC_TAU_D | 
| AUMC all linear | AUMC_all_lin | AUMCALL | Not calculated |
| AUMC all linlog | AUMC_all_log | AUMCALL | Not calculated |
| AUMC infinity linear | AUMC_inf_lin | AUMCIFO | AUMCINF | 
| AUMC infinity linear C0 | AUMC_inf_lin_C0 | AUMC_inf_lin | AUMCIFO | AUMCINF | 
| AUMC infinity linlog | AUMC_inf_log | AUMCIFO | AUMCINF | 
| AUMC infinity linlog C0 | AUMC_inf_log_C0 | AUMC_inf_lin | AUMCIFO | AUMCINF | 
| AUMC last linear | AUMC_last_lin | AUMCLST | AUMClast |
| AUMC last linear C0 | AUMC_last_lin_C0 | AUMCLST | AUMClast |
| AUMC last linlog | AUMC_last_log | AUMCLST | AUMClast |
| AUMC last linlog C0 | AUMC_last_log_C0 | AUMCLST | AUMClast |
| AUMC Tau linear | AUMC_tau_lin | AUMCTAU | Not calculated |
| AUMC Tau linear C0 | AUMC_tau_lin_C0 | AUMCTAU | Not calculated | 
| AUMC Tau linlog | AUMC_tau_log | AUMCTAU | Not calculated |
| AUMC Tau linlog C0 | AUMC_tau_log_C0 | AUMCTAU | Not calculated | 
| Average concentration linear | Cavg_lin | CAVG | Cavg |
| Average concentration linlog | Cavg_log | CAVG | Cavg |
| C0 | C0 | C0 | C0 |
| Cmax/Dose | Cmax_D | CMAXD | Cmax |
| CL linear | CL_lin_C0 | CLO | Cl_obs | 
| CL linlog | CL_log_C0 | CLO | Cl_obs | 
| CL/F linear | CL_f_lin | CLFO | CL_F_obs |
| CL/F linlog | CL_f_log | CLFO | CL_F_obs | 
| CLss/F linear | CLss_F_lin | None | CLss_F | 
| CLss/F linlog | CLss_F_log | None | CLss_F | 
| Dose | Dose | NA | Dose |
| Fluctuation linear | Fluct_lin | FLUCTP | Fluctuation% |
| Fluctuation linlog | Fluct_log | FLUCTP | Fluctuation% |
| Fluctuation Tau linear | Fluct_tau_lin | FLUCTP | Fluctuation%_Tau |
| Fluctuation Tau linlog | Fluct_tau_log | FLUCTP | Fluctuation%_Tau |
| Lag time | Tlag | TLAG | Tlag |
| Last measurable concentration | Clast | CLST | Clast |
| Maximum concentration | Cmax | CMAX | Cmax |
| Minimum concentration | Cmin | CMIN | Cmin |
| MRT last linear | MRT_last_lin | MRTEVLST (extravascular), MRTIBLST (iv bolus), MRTICLST (iv infusion) | MRTlast | 
| MRT last linear | MRT_last_lin_C0 | MRTIBLST (iv bolus) | MRTlast |
| MRT last linlog | MRT_last_log | MRTEVLST (extravascular), MRTIBLST (iv bolus), MRTICLST (iv infusion) | MRTlast |  
| MRT last linlog | MRT_last_log_C0 | MRTIBLST (iv bolus) | MRTlast |
| MRT linear | MRT_lin | MRTEVIFO (extravascular), MRTIBIFO (iv bolus), MRTICIFO (iv infusion) | MRTINF_obs |
| MRT linear | MRT_lin_C0 | MRTIBIFO (iv bolus) | MRTINF_obs |
| MRT linlog | MRT_log | MRTEVIFO (extravascular), MRTIBIFO (iv bolus), MRTICIFO (iv infusion) | MRTINF_obs | 
| MRT linlog | MRT_log_C0 | MRTIBIFO (iv bolus) | MRTINF_obs | 
| Number of BLQ samples | N_blq | None | Not provided |
| Number of data points in terminal slope calculation | kel_n | LAMZNPT | Not provided | 
| Number of missing samples | N_miss | None | Not provided |
| Number of samples | N_samp | None | N_Samples |
| Partial AUC from C0 linear | pAUC_C0_lin | None | Not provided |
| Partial AUC from C0 linlog | pAUC_C0_log | None | Not provided |
| Percent AUC extrapolated to C0 linear | AUC_extrap_C0_lin | AUCPBEO | AUC_%Back_Ext_obs |
| Percent AUC extrapolated to C0 linlog | AUC_extrap_C0_log | AUCPBEO | AUC_%Back_Ext_obs |
| Percent extrapolated AUC infinity linear | AUC_inf_lin_extrap | AUCPEO | AUC_%Extrap_obs | 
| Percent extrapolated AUC infinity linear C0 | AUC_inf_lin_C0_extrap | AUCPEO | AUC_%Extrap_obs | 
| Percent extrapolated AUC infinity linlog | AUC_inf_log_extrap | AUCPEO | AUC_%Extrap_obs | 
| Percent extrapolated AUC infinity linlog C0 | AUC_inf_log_C0_extrap | AUCPEO | AUC_%Extrap_obs | 
| Percent extrapolated AUC Tau linear | None | AUC_TAU_%Extrap | 
| Percent extrapolated AUC Tau linear C0 | None | AUC_TAU_%Extrap | 
| Percent extrapolated AUC Tau linlog | AUC_tau_log_extrap | None | AUC_TAU_%Extrap | 
| Percent extrapolated AUC Tau linlog C0 | None | AUC_TAU_%Extrap | 
| Percent extrapolated AUMC infinity linear | AUMC_inf_lin_extrap | AUMCPEO | AUMC_%Extrap_obs | 
| Percent extrapolated AUMC infinity linear C0 | AUMC_inf_lin_C0_extrap | AUMCPEO | AUMC_%Extrap_obs | 
| Percent extrapolated AUMC infinity linlog | AUMC_inf_log_extrap | AUMCPEO | AUMC_%Extrap_obs | 
| Percent extrapolated AUMC infinity linlog C0 | AUMC_inf_lin_C0_extrap | AUMCPEO | AUMC_%Extrap_obs | 
| Swing | Swing | SWING | Swing | 
| Swing with Ctau | Swing_Tau | SWING | Swing_Tau |
| Tau | tau | TAU | Tau |
| Terminal slope intercept | intercept | NA | Lambda_z_intercept | 
| Terminal slope | kel | LAMZ | lambda_z |
| Terminal slope adjusted r-squared | kel_adjr2 | NA | Lambda_z_adjr2 | 
| Terminal slope lower time point | kel_low | LAMZLL | Lambda_z_lower | 
| Terminal slope r-squared | kel_r2 | NA | Lambda_z_r2 | 
| Terminal slope span | kel_span | LAMZSPN | Span |
| Terminal half life | kel_thalf | LAMZHL | thalf | 
| Terminal slope upper time point | kel_upper | LAMZUL | Lambda_z_upper |
| Time of Dose | Dose_time | NA | Dosing time |
| Time of Clast | Tlast | TLST | Tlast |
| Time of Cmax | Tmax | TMAX | Tmax |
| Time of Cmin | Tmin | TMIN | Tmin |
| Trough concentration | Ctau | CTROUGH | Not provided |
| Vz linear | Vz_lin_C0 | VZO | Vz_F |
| Vz linlog | Vz_log_C0 | VZO | Vz_F |
| Vz/F linear | Vz_f_lin | VZFO | Vz_F_obs | 
| Vz/F linlog | Vz_f_log | VZFO | Vz_F_obs | 
| Vss linear | Vss_lin_C0 | VSSO | Vss_obs |
| Vss linlog | Vss_log_C0 | VSSO | Vss_obs |

Note: Phoenix WinNonlin also provides parameters with the suffix "_pred" such as MRTINF_pred, AUCINF_pred. These parameters are calculated by replacing the observed concentration at Clast with a predicted concentration based on the estimated terminal slope value. These "_pred" parameters are not accepted by regulatory authorities as representative of the observed data. These "_pred" parameters were thought to be better approximations of parameter values to support model fitting work; however, with the improvements in model fitting algorithms, the use of these "_pred" parameters is no longer needed.
