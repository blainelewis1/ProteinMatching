from utils import *

import math

ERROR = 0.5

def process_spectrum(mass, spectrum_data, all_peptides, sorted_masses_peptides, scan_number):

	count = 0
	matches = []


	#for peptide_mass in all_peptides.keys():
	#	if mass - 0.5 <= peptide_mass and mass + 0.5 >= peptide_mass:
	#		count += 1
	#		matches.append(peptide_mass)

	candidate_peptides = binary_error_search(sorted_masses_peptides, mass, 0.5)

	#print(candidate_peptides, matches)
	#print(len(candidate_peptides), count)
	#assert(len(candidate_peptides) == count)


	scores = dict()

	spectrum_masses = sorted([item[0] for item in spectrum_data])
	spectrum_data = {item[0]: item[1] for item in spectrum_data}

	temp_poss_peps = []


	for candidate_peptide in candidate_peptides:
		temp_poss_peps += all_peptides[candidate_peptide]

	candidate_peptides = temp_poss_peps

	#print(candidate_peptides)

	cur_max_score = 0
	cur_max_peptide = None

	for peptide in candidate_peptides:

		score = 0

		y_ions = peptide[1]

		for y_ion in y_ions:
			
			y_ion += 19.018

			candidate_masses = binary_error_search(spectrum_masses, y_ion, ERROR)

			for candidate_mass in candidate_masses:
				score += math.log(1 + 100 * spectrum_data[candidate_mass])

		if(score > cur_max_score):
			cur_max_score = score
			cur_max_peptide = peptide
	

	if(cur_max_peptide):
		print(cur_max_peptide[0], cur_max_score, [item[0] for item in candidate_peptides], scan_number, mass, sep='\t')
	else:
		print('None\t0\t0\t0')


	return cur_max_peptide
