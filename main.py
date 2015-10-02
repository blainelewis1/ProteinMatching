

def parseMgf():		
	with open('test.mgf') as file:
		scan_number = 0
		total_mass = 0

		data = []

		for line in file:
			line = line.strip()

			if line == "BEGIN IONS":
				#TODO
				scan_number = 0
				data = []
				total_mass = 0
			
			elif line.startswith("TITLE") or line.startswith("CHARGE") or line.startswith("RTINSECONDS"):
				continue
			
			elif line.startswith("PEPMASS"):
				total_mass = float(line.split("=")[1])
			
			elif line == "END IONS":
				# TODO process
				# normalize data
				data = normalize_data(data)
				process_spectrum(total_mass, data, dictionary)				
				continue
			
			elif line.startswith("SCANS"):
				scan_number = line.split("=")[1]

			else:
				tokens = line.split(" ")
				print(tokens)
				data.append((float(tokens[0]), float(tokens[1])))




def normalize_data(data):
	max_value = max(data, key = lambda item: item[1])[1]
	
	return [(item[0], item[1]/max_value) for item in data]


def main():
	parseMgf()

if __name__ == "__main__":
	main()
