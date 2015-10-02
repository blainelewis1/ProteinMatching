from utils import *

import math

ERROR = 0.5

def process_spectrum(mass, spectrum_data, all_peptides, sorted_masses_peptides, scan_number):

	possible_peptides = binary_error_search(sorted_masses_peptides, mass, 0.5)

	scores = dict()

	spectrum_masses = sorted([item[0] for item in spectrum_data])
	spectrum_data = {item[0]: item[1] for item in spectrum_data}

	temp_poss_peps = []


	for possible_peptide in possible_peptides:
		temp_poss_peps += all_peptides[possible_peptide]

	possible_peptides = temp_poss_peps

	cur_max_score = 0
	cur_max_peptide = None

	for peptide in possible_peptides:

		score = 0

		y_ions = peptide[1]

		for y_ion in y_ions:
			
			y_ion += 19.018

			possible_masses = binary_error_search(spectrum_masses, y_ion, ERROR)

			for possible_mass in possible_masses:
				score += math.log(1 + 100 * spectrum_data[possible_mass])

		if(score > cur_max_score):
			cur_max_score = score
			cur_max_peptide = peptide
	

	if(cur_max_peptide):
		print(cur_max_peptide[0], cur_max_score, [item[0] for item in possible_peptides], scan_number, sep=',')
	else:
		print('None,0,0,0')


	return cur_max_peptide

