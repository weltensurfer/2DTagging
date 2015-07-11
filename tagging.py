#!/usr/bin/python

import ROOT
import argparse
from jec.tagging import jet2DTagging

parser = argparse.ArgumentParser(description='2DTagging Tool')

parser.add_argument('-m', '--mc', nargs='?', required=True)
parser.add_argument('-d', '--data', nargs='?', default=None)
parser.add_argument('-f', '--filename', nargs='?', default='output/results.root')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()

mc_file = ROOT.TFile(args.mc)
data_file = None
if args.data is not None:
	data_file = ROOT.TFile(args.data)

mc_plots = {}
data_plots = {}
for zone in ['1Q', '3C', '4B', '2G']:
	nick = "MC_MPF_Zone"+zone
	mc_plots[nick] = mc_file.Get(nick)
	for flavour in ['uds', 'c', 'b', 'g']:
		nick = "MC_MPF_Zone"+zone+"_"+flavour
		mc_plots[nick] = mc_file.Get(nick)

	if data_file is not None:
		nick = "Data_MPF_Zone"+zone
		data_plots[nick] = data_file.Get(nick)

tagging = jet2DTagging(mc_plots, data_plots)
output_file = ROOT.TFile(args.filename, "recreate")

result_mc = tagging.getFlavourResponsePlot('MC')
print "Results for MC:"
result_mc.Print()
result_mc.Write()
if data_file is not None:
	result_data = tagging.getFlavourResponsePlot('Data')
	print "Results for Data:"
	result_data.Print()
	result_data.Write()
output_file.Close()
print "Write output to: %s" % (output_file.GetPath())

