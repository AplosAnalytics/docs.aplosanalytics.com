# 🟨 Area Under the Moment Curve

The area under the moment curve (AUMC) is a measure of the total area under the first moment curve. The Moment Curve is a paired set of values (x,y) where x is the time and y is the time multiplied by the concentration from the concentration-time curve. Just as [AUC](aucmethods.md) is calculated using partial areas, the AUMC is calculated using partial areas for the moment curve ($pAUMC$). The $pAUMCs$ can be calculated using the [linear method](#linear-method) or [linear up logarithmic down method](#linear-up-logarithmic-down-method). 

The [linear method](#linear-method) is the most commonly used calculation of AUMC because there is no assumption of exponential decline in the first moment curve (contrary to the concentration-time curve which normally exhibits exponential decline). However, both methods are performed in Aplos NCA for the user. 

## Linear Method

The following equation is used to calculate the $pAUMC$ between any two data points with concentration values:

$$ pAUMC={{1} \over {2}} * ({C2 * T2} + {C1 * T1}) * (T2 - T1) $$

## Linear Up Logarithmic Down method

The following equation is used to calculate the $pAUMC$ for any two data points with concentration values which are increasing, or when either concentration value is 0:

$$ pAUMC={{1} \over {2}} * ({C2 * T2} + {C1 * T1}) * (T2 - T1) $$

When the concentrations are declining, and neither concentration value is 0, the following equation is used to calculate the $pAUMC$:

$$ pAUMC = [{{C1 * T1 - C2 * T2} \over {ln({{C1} \over {C2}})}}] * (T2 - T1)-{{C2-C1} \over {ln({{C2} \over {C1}})}} * {(T2-T1)}^2 $$