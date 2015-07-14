# Flavour Response #

## Introduction ##
This Repository contains standalone tools for flavour response studies.
Currently this includes the matrix inversion of the 2DTagging method.

## Dependencies ##

* `Python`
	* `pyroot` for accessing root files

### Python ###
The entire code is written in **python**, specifically for the `python2` LTS version `2.7`.

## 2DTagging Method ##
This tool extracts the MC-Truth flavour composition and the MPF response in each zone from the input histogramms and determine the jet response for each flavour (uds, c, b and gluon) using the matrix inversion.

### Input Format ###
The input format are separate root files for monte carlo and data containing all required histogramms.  
Required histogramms are MPF response plots including all flavours and for each flavour in a tagging zone.  

#### Monte Carlo ####
```
ROOT TFile
- TH1D MC_MPF_Zone1Q
- TH1D MC_MPF_Zone1Q_uds
- TH1D MC_MPF_Zone1Q_c
- TH1D MC_MPF_Zone1Q_b
- TH1D MC_MPF_Zone2G
- TH1D MC_MPF_Zone2G_uds
- TH1D MC_MPF_Zone2G_c
- TH1D MC_MPF_Zone2G_b
- TH1D MC_MPF_Zone3C
- TH1D MC_MPF_Zone3C_uds
- TH1D MC_MPF_Zone3C_c
- TH1D MC_MPF_Zone3C_b
- TH1D MC_MPF_Zone4B
- TH1D MC_MPF_Zone4B_uds
- TH1D MC_MPF_Zone4B_c
- TH1D MC_MPF_Zone4B_b
```

#### Data ####
```
ROOT TFile
- TH1D Data_MPF_Zone1Q
- TH1D Data_MPF_Zone2G
- TH1D Data_MPF_Zone3C
- TH1D Data_MPF_Zone4B
```

### Example ###

```
./tagging.py --mc examples/ZJet_mc2012_2015-07-14.root --data examples/ZJet_data2012_2015-07-14.root

```
