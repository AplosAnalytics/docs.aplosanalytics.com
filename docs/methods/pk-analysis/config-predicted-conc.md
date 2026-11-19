# 🟢 Predicted Concentrations

Predicted concentrations report the concentration at specific time points that you choose, even when no sample was collected at that time. The user supplies a list of one or more times (decimals are allowed). The times are assumed to be in the same units as the time variable in the dataset.

For each requested time, two parameters are reported:

* **paramcd**: `pred_c_{time}_lin` and `pred_c_{time}_log`. The decimal point in the time is replaced with an underscore and trailing zeros are dropped. For example, a time of 0.25 produces `pred_c_0_25_lin` and `pred_c_0_25_log`, and a time of 24 produces `pred_c_24_lin` and `pred_c_24_log`.
* **param**: "Predicted concentration at time = {time}", for example "Predicted concentration at time = 0.25".

The output units are the concentration units of the profile.

## Calculation method

1. If a concentration was observed at the requested time, the observed value is reported for both `_lin` and `_log`.
2. If no concentration was observed at the requested time, and there are observed samples both before and after it, the concentration is imputed from the two adjacent samples:
    * `_lin` uses [linear interpolation](../extrapolationmethods).
    * `_log` uses [linear interpolation](../extrapolationmethods) when the concentration is increasing or flat between the two samples, and [logarithmic interpolation](../extrapolationmethods) when the concentration is decreasing. If either concentration is zero, linear interpolation is used because the logarithm of zero is undefined.
3. If no concentration was observed at the requested time and there is not a sample both before and after it, the value is reported as "ND" for both `_lin` and `_log`, and a message is added to the non-fatal warnings: "Concentration at time = {time} could not be predicted because there was not a sample both before and after the requested time."

> [!NOTE]
> Predicted concentrations are never extrapolated. A time before the first sample or after the last sample is reported as ND.

> [!NOTE]
> If the same time is listed more than once, it is calculated once and a warning is reported. Times must be zero or greater.

## Manual JSON structure

If you are performing analysis using a formatted JSON file, the "predicted_conc" section is at the top level of the configuration JSON and is an array of numbers:

```js
{
  "predicted_conc": [0.25, 0.45, 1.5, 3.25, 24]
}
```
