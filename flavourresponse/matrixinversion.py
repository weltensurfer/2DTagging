import ROOT
import numpy as np


class MatrixInversion:
	zones = ['1Q', '3C', '4B', '2G']
	flavours = ['uds', 'c', 'b', 'g']

	def __init__(self, plots, debug=False):
		self._plots = plots
		self._debug = debug

	def get_mean_mpf_values(self, prefix):
		if prefix not in ['MC', 'Data']:
			raise ValueError

		mean_mpf_values = []
		mean_mpf_values_up = []
		mean_mpf_values_down = []
		for zone in self.zones:
			plot = self._plots[prefix + "_MPF_Zone" + zone]
			mean_mpf_values.append(plot.GetMean())
			mean_mpf_values_up.append(mean_mpf_values[-1] + plot.GetMeanError())
			mean_mpf_values_down.append(mean_mpf_values[-1] - plot.GetMeanError())

		return np.array(mean_mpf_values), np.array(mean_mpf_values_up), np.array(mean_mpf_values_down)

	def get_flavour_fractions(self):
		flavour_fractions = []
		for zone in self.zones:
			zone_fractions = []
			all_plot = self._plots["MC_MPF_Zone" + zone]
			sum_all = all_plot.Integral()
			for flavour in self.flavours:
				plot = self._plots["MC_MPF_Zone" + zone + "_" + flavour]
				flavour_sum = plot.Integral()
				zone_fractions.append(flavour_sum / sum_all)
			flavour_fractions.append(zone_fractions)
		return np.array(flavour_fractions)

	def get_flavour_responses(self, prefix):
		mean_mpf_values, mean_mpf_values_up, mean_mpf_values_down = self.get_mean_mpf_values(prefix)
		flavour_fractions = self.get_flavour_fractions()

		response_for_flavour = np.linalg.solve(flavour_fractions, mean_mpf_values)
		response_for_flavour_up = np.linalg.solve(flavour_fractions, mean_mpf_values_up)
		response_for_flavour_down = np.linalg.solve(flavour_fractions, mean_mpf_values_down)

		return response_for_flavour, response_for_flavour_up, response_for_flavour_down

	def get_flavour_response_plot(self, prefix):
		result_plot = ROOT.TGraphAsymmErrors()
		result_plot.SetName(prefix + "_MPF_Zones_Flavour_Response")

		response_for_flavour, response_for_flavour_up, response_for_flavour_down = self.get_flavour_responses(prefix)
		for i in xrange(len(self.flavours)):
			result_plot.SetPoint(i, i + 1, response_for_flavour[i])
			result_plot.SetPointEYhigh(i, response_for_flavour_up[i] - response_for_flavour[i])
			result_plot.SetPointEYlow(i, response_for_flavour[i] - response_for_flavour_down[i])

		return result_plot
