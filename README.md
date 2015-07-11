# 2DTagging #

## Introduction ##


## Dependencies ##

* `Python`
	* `pyroot` for accessing root files

### Python ###
The entire code is written in **python**, specifically for the `python2` LTS version `2.7`.

#### RHEL6/SL6 ####
`python2.7` is available from the `scl_python27` repository.

## Input Format ##

The input format are separate root files for monte carlo and data containing all required histogramms.  

### Monte Carlo ###
```
ROOT TFile
- TH1D MC_MPF_Zone1Q
- TH1D MC_MPF_Zone1Q_uds
- TH1D MC_MPF_Zone1Q_c
- TH1D MC_MPF_Zone1Q_b
- TH1D MC_MPF_Zone1Q_undef
- TH1D MC_MPF_Zone2G
- TH1D MC_MPF_Zone2G_uds
- TH1D MC_MPF_Zone2G_c
- TH1D MC_MPF_Zone2G_b
- TH1D MC_MPF_Zone2G_undef 
- TH1D MC_MPF_Zone3C
- TH1D MC_MPF_Zone3C_uds
- TH1D MC_MPF_Zone3C_c
- TH1D MC_MPF_Zone3C_b
- TH1D MC_MPF_Zone3C_undef 
- TH1D MC_MPF_Zone4B
- TH1D MC_MPF_Zone4B_uds
- TH1D MC_MPF_Zone4B_c
- TH1D MC_MPF_Zone4B_b
- TH1D MC_MPF_Zone4B_undef
```

### Data ###
```
ROOT TFile
- TH1D Data_MPF_Zone1Q
- TH1D Data_MPF_Zone2G
- TH1D Data_MPF_Zone3C
- TH1D Data_MPF_Zone4B
```

## Example ##

```
./tagging.py --mc mc.root --data data.root

```