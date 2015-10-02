def process_spectrum(mass, spectrum_data, all_peptides, sorted_masses_peptides):
	possible_peptides = binary_error_search(sorted(all_peptides.keys()), mass, 0.5)
	masses = spectrum_data
	scores = dict()

	for peptide in all_peptides:
		
		score = 0
		y_ion = peptide[1]

		for suffix in all_peptides:
			binary_error_search()
			all_peptides


		scores[peptide] = score
