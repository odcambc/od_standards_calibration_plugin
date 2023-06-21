
## Pioreactor OD standards calibration plugin

The standard dilution-based OD calibration system is not always ideal for setting up a cluster of Pioreactors. This plugin allows you to calibrate a Pioreactor using a series of samples with known OD, rather than serially diluting a starting sample. Note, however, that the quality of the calibration will depend on the number of samples and the range of ODs used. This is a drop-in replacement for the standard OD calibration, and does not change the behavior of OD measurements after calibration. 

## Run your calibration

Type into your command line:

```
pio run od_calibration_from_standards
```

To perform this calibration, insert your vial containing media into the Pioreactor and submerge your light probe. Follow the prompts on the command line. The plugin will increase the light intensity, and prompt you to record the readings from your light probe. A calibration line of best fit will be generated based on your light probe readings.

