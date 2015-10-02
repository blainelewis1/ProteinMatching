import re
import collections

masses = {"A" : 71.03711, "R" : 156.10111, "N" : 114.04293, "D" : 115.02694, "C" : 103.00919 + 57.02, "E" : 129.04259, "Q" : 128.05858, "G" : 57.02146, "H" : 137.05891, "I": 113.08406, "L" : 113.08406, "K" : 128.09496, "M" : 131.04049, "F" : 147.06841, "P": 97.05276, "S" : 87.03203, "T" : 101.04768, "W" : 186.07931, "Y" : 163.06333, "V" : 99.06841}

pepDict = {} # mass : [   (string, [masses])  ]

def calculateMasses(pep):
	peptides = list(pep)
	pepMasses = [masses[peptides[-1]]]
	for i in reversed(peptides[:-1]):
		pepMasses.insert(0, masses[i] + pepMasses[0])
	return pepMasses

def splice(line):
	indicesKR = [i.start()+1 for i in re.finditer('(K|R)', line)]
	indicesNotP = [i.start()+1 for i in re.finditer('(KP|RP)', line)]
	split = set(indicesKR) - set (indicesNotP)
	return partition(line, sorted(list(split)))

def partition(alist, indices):
	return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]

def repeats(values, p):
	for t in values:
		if t[0] == p:
			return True
	return False

def parseFasta():
	with open('ups.fasta') as f:
		for line in f:
			if line[0:1] != ">":
				tryp = filter(None, splice(line.strip()))
				for p in tryp:
					massTryp = calculateMasses(p)
					if massTryp[0] in pepDict:
						if not repeats(pepDict[massTryp[0]], p):
							pepDict[massTryp[0]].append((p, massTryp))
					else:
						pepDict[massTryp[0]] = [(p, massTryp)]
	print pepDict

parseFasta()


