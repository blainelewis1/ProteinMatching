
ERROR = 0.5

def process_spectrum(mass, spectrum_data, all_peptides, sorted_masses_peptides):

	possible_peptides = binary_error_search(sorted(all_peptides.keys()), mass, 0.5)
	masses = spectrum_data
	scores = dict()

	spectrum_masses = [item[0] for item in range(len(spectrum_data))]
	spectrum_data = {item[0]: item[1] for item in range(len(spectrum_data))}

	for peptide in all_peptides:
		
		score = 0
		y_ions = peptide[1]

		for y_ion in y_ions.reverse():
			
			binary_error_search(spectrum_masses, y_ion, ERROR)
			all_peptides

		scores[peptide] = score

