from process_spectrum import process_spectrum
from parse_fasta import parse_fasta
from utils import *

def parse_mgf(filename,all_peptides,sorted_masses_peptides):		
	with open(filename) as file:
		scan_number = 0
		pep_mass = 0
		charge = 0

		spectrum_data = []

		for line in file:
			line = line.strip()

			if line == "BEGIN IONS":
				#TODO
				scan_number = 0
				spectrum_data = []
				total_mass = 0
			
			elif not line or line.startswith("TITLE") or line.startswith("RTINSECONDS"):
				continue

			elif line.startswith("CHARGE"):
				charge = int(line.split("=")[1][0])
			
			elif line.startswith("PEPMASS"):
				pep_mass = float(line.split("=")[1]) # is this peptide mass?
			
			elif line == "END IONS":
				# TODO process
				# normalize data
				spectrum_data = normalize_data(spectrum_data)
				
				# todo: compute proper mass based on formula 
				total_mass = (pep_mass - 1.007)*charge - 18.01

				process_spectrum(total_mass, spectrum_data, all_peptides, sorted_masses_peptides, scan_number)						

			
			elif line.startswith("SCANS"):
				scan_number = line.split("=")[1]

			else:
				tokens = line.split(" ")

				spectrum_data.append((float(tokens[0]), float(tokens[1])))



def main():
	all_peptides = parse_fasta("bigger.fasta") # is a dictionary in the form of ... mass -> [(string,suffixMasses),...]	
	sorted_masses_peptides = sorted(all_peptides.keys())
	parse_mgf("test.mgf",all_peptides,sorted_masses_peptides)

if __name__ == "__main__":
	main()

#print(binary_error_search([1,2,3,4,5], 3, 1))
#print(binary_error_search([1,2,3,4,5], 3, 0))
#print(binary_error_search([1,2,3,4,5], 3, 2))
#print(binary_error_search([1,2,3,5,6,7,8,9], 4, 0))
#print(binary_error_search([0,1,2,8,9,10], 5, 0.5))
#print(binary_error_search([0,1,2,8,9,10], 5, 3))