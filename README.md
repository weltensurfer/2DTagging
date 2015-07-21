# Flavour Response #

## Introduction ##
This Repository contains standalone tools for CMS flavour response studies.
Currently this includes the matrix inversion of the 2DTagging method.

More information can be found at the corresponding [twiki page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/JESFlavorStudies "JES Flavour twiki")

## Dependencies ##
The entire code is written in **python**, specifically for the `python2` LTS version `2.7`.
* Needed python packages:
	* `pyroot` for handling root files and histograms
	* `numpy` for calculations

## 2DTagging Method ##
This tool extracts the MC-Truth flavour composition and the MPF response in each zone from the input histogramms and determines the jet response for each flavour (uds, c, b and gluon) using the matrix inversion.

### Input Format ###
The input format are separate root files for Data and Monte Carlo containing all required histogramms: 
* For MC:  MPF response distributions for all flavours (uds/c/b/g/inclusive) in each tagging zone (Q,G,B,C)
* For Data: MPF response distributions for each tagging zone (Q,G,B,C)

#### Monte Carlo ####
```
ROOT TFile
- TH1D MC_MPF_Zone1Q
- TH1D MC_MPF_Zone1Q_uds
- TH1D MC_MPF_Zone1Q_c
- TH1D MC_MPF_Zone1Q_b
- TH1D MC_MPF_Zone1Q_g
- TH1D MC_MPF_Zone2G
- TH1D MC_MPF_Zone2G_uds
- TH1D MC_MPF_Zone2G_c
- TH1D MC_MPF_Zone2G_b
- TH1D MC_MPF_Zone2G_g
- TH1D MC_MPF_Zone3C
- TH1D MC_MPF_Zone3C_uds
- TH1D MC_MPF_Zone3C_c
- TH1D MC_MPF_Zone3C_b
- TH1D MC_MPF_Zone3C_g
- TH1D MC_MPF_Zone4B
- TH1D MC_MPF_Zone4B_uds
- TH1D MC_MPF_Zone4B_c
- TH1D MC_MPF_Zone4B_b
- TH1D MC_MPF_Zone4B_g
```

#### Data ####
```
ROOT TFile
- TH1D Data_MPF_Zone1Q
- TH1D Data_MPF_Zone2G
- TH1D Data_MPF_Zone3C
- TH1D Data_MPF_Zone4B
```

### Example Usage ###
Execute the `tagging.py` script with the data and MC files as argument:
```
`./tagging.py --mc examples/ZJet_mc2012_2015-07-14.root --data examples/ZJet_data2012_2015-07-14.root`

```
