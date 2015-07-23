#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ROOT
import argparse
import errno

from flavourresponse.matrixinversion import MatrixInversion


def print_responses(entrys, type_label):
	print "+----------+----------------+----------------+"
	print "|%-10s|%-16s|%-16s|" % (type_label, "MC", "Data")
	print "+----------+----------------+----------------+"
	for entry in entrys:
		mc_response = " %.3f +- %.3f" % (round(entry['mc'], 3), round(entry['mc_err'], 3))
		if entry['data'] is None or entry['data_err'] is None:
			data_response = ""
		else:
			data_response = " %.3f +- %.3f" % (round(entry['data'], 3), round(entry['data_err'], 3))
		print u"|%-10s|%-16s|%-16s|" % (entry['type'], mc_response, data_response)
	print "+----------+----------------+----------------+"

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

	#get input histograms and print zone responses
	plots = {}
	zone_responses = []
	for zone in MatrixInversion.zones:
		zone_response = {
			'type': zone,
			'mc': None,
			'mc_err': None,
			'data': None,
			'data_err': None
		}
		nick = "MC_MPF_Zone" + zone
		plots[nick] = mc_file.Get(nick)
		zone_response['mc'] = plots[nick].GetMean()
		zone_response['mc_err'] = plots[nick].GetMeanError()
		for flavour in MatrixInversion.flavours:
			nick = "MC_MPF_Zone" + zone + "_" + flavour
			plots[nick] = mc_file.Get(nick)

		if data_file is not None:
			nick = "Data_MPF_Zone" + zone
			plots[nick] = data_file.Get(nick)
			zone_response['data'] = plots[nick].GetMean()
			zone_response['data_err'] = plots[nick].GetMeanError()
		zone_responses.append(zone_response)
	print "Jet response values for each zone:"
	print_responses(zone_responses, "Zone")

	#perform matrix inversion, display results and write to file
	try:
		 os.makedirs(args.filename)
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	output_file = ROOT.TFile(args.filename, "RECREATE")

	tagging = MatrixInversion(plots)

	result_mc = tagging.get_flavour_response_plot('MC')

	result_mc.Write()
	result_data = None
	if data_file is not None:
		result_data = tagging.get_flavour_response_plot('Data')
		result_data.Write()

	flavour_responses = []
	for flavour, i in zip(MatrixInversion.flavours, xrange(len(MatrixInversion.flavours))):
		mcX, mcY, dataX, dataY, dataErr = ROOT.Double(0), ROOT.Double(0), ROOT.Double(0), ROOT.Double(0), None
		result_mc.GetPoint(i, mcX, mcY)
		if result_data is not None:
			result_data.GetPoint(i, dataX, dataY)
			dataErr = result_data.GetErrorY(i)
		else:
			dataY = None
		flavour_response = {
			'type': flavour,
			'mc': mcY,
			'mc_err': result_mc.GetErrorY(i),
			'data': dataY,
			'data_err': dataErr
		}

		flavour_responses.append(flavour_response)
	print "Jet response values for each flavour:"
	print_responses(flavour_responses, "Flavour")

	print "\nWrite output to: %s" % (output_file.GetPath())
	output_file.Close()
	mc_file.Close()
	data_file.Close()

if __name__ == "__main__":
	main()
