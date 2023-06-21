
## Pioreactor OD standards calibration plugin

The standard dilution-based OD calibration system is not always ideal for setting up a cluster of Pioreactors. This plugin allows you to calibrate a Pioreactor using a series of samples with known OD, rather than serially diluting a starting sample. Note, however, that the quality of the calibration will depend on the number of samples and the range of ODs used. This is a drop-in replacement for the standard OD calibration, and does not change the behavior of OD measurements after calibration. 

## Run your calibration

Type into your command line:

```
pio run od_calibration_from_standards
```

To perform this calibration, prepare a set of standards in individual vials with known OD (at least 10 mL volume) and with stir bars. Run the above command and follow the prompts. A calibration based on fitting will be produced.
