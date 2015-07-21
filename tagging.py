#!/usr/bin/python
# -*- coding: utf-8 -*-

import ROOT
import argparse

from flavourresponse.matrixinversion import MatrixInversion


def main():
	"""Read input histograms from file, perfrom matrix inversion and save results."""

	#get arguments
	parser = argparse.ArgumentParser(description='2DTagging Tool')
	parser.add_argument('-m', '--mc', nargs='?', required=True)
	parser.add_argument('-d', '--data', nargs='?', default=None)
	parser.add_argument('-f', '--filename', nargs='?', default='output/results.root')
	parser.add_argument('--debug', action='store_true')
	args = parser.parse_args()

	#open input files
	mc_file = ROOT.TFile(args.mc)
	data_file = None
	if args.data is not None:
		data_file = ROOT.TFile(args.data)

	#get input histograms
	plots = {}
	for zone in MatrixInversion.zones:
		nick = "MC_MPF_Zone" + zone
		plots[nick] = mc_file.Get(nick)
		for flavour in MatrixInversion.flavours:
			nick = "MC_MPF_Zone" + zone + "_" + flavour
			plots[nick] = mc_file.Get(nick)

		if data_file is not None:
			nick = "Data_MPF_Zone" + zone
			plots[nick] = data_file.Get(nick)

	mc_file.Close()
	data_file.Close()

	#TODO: print values before inversion

	#perform matrix inversion, display results and write to file
	output_file = ROOT.TFile(args.filename, "RECREATE")

	tagging = MatrixInversion(plots)

	result_mc = tagging.get_flavour_response_plot('MC')
	print "\nResults for MC:"
	result_mc.Print()

	#TODO: nicer output

	result_mc.Write()
	if data_file is not None:
		result_data = tagging.get_flavour_response_plot('Data')
		print "\nResults for Data:"
		result_data.Print()
		result_data.Write()
	output_file.Close()
	print "\nWrite output to: %s" % (output_file.GetPath())


if __name__ == "__main__":
	main()
