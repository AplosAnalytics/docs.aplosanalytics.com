# 🟪 Extrapolation and Interpolation Methods
Various extrapolation and interpolation methods are used during the calculation of some PK parameters. The mathematical expressions for these methods are shown below.

## Linear interpolation
If a concentration value must be interpolated between two observed concentration values using linear interpolation, the following equation will be used:

$$ C_{interpolated} = C1 + \vert{{T_{interpolated} - T1} \over {T2 - T1}}\vert * (C2 - C1) $$

## Logarithimic interpolation

If a concentration value must be interpolated between two observed concentration values using logarithmic interpolation, the following equation will be used:

$$ C_{interpolated} = e^{[ln(C1) + \vert{{T_{interpolated} - T1} \over {T2 - T1}}\vert * [ln(C2) - ln(C1)]]} $$

## Logarithmic extrapolation for Ctau
If a value of Ctau is not observed in the dataset, it can be estimated by extrapolating from the last observed concentration using the following equation:

$$ Ctau = Clast * e^{-kel * (T_{Tau} - Tlast)} $$

## Logarithim extrapolation for C0
Backward extrapolation to estimate the concentration at time 0 is performed using the first 2 measured concentrations following dose administration. The first step is to perform a linear regression and estimating the slope ($m$) and intercept ($b$) using the following equation:

$$ y = m*[ln(C)] + b $$

Then the value for C0 is calculated using the following equation:

$$ C0 = e^b $$
