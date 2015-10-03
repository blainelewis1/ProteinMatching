#!/usr/bin/env python
# @author mathew teoh
import csv 
import ast

def parseTestFile():
	testscanpeps = []
	dict_testscanpeps = {}
	# size = 0
	with open('commercial.csv','rt') as csvfile:
		testread = csv.reader(csvfile,delimiter=',')
		next(testread)
		for row in testread:
			# print(row)
			# print(row[0])
			testpeptide = remove_dat_hoohah(row[0])
			scannum = row[6]
			print(testpeptide)
			# print(scannum)
			testscanpeps.append([scannum,testpeptide])
			# size = size + 1
			# assert size == len(testscanpeps)
			dict_testscanpeps[scannum] = len(testscanpeps)

	return testscanpeps, dict_testscanpeps

def remove_dat_hoohah(testpeptide):
	return testpeptide.replace("(+57.02)","")

def parseResultsFile():
	resultpeps = []
	with open('results.tsv','rt') as csvfile:
		resread = csv.reader(csvfile,delimiter='\t')
		for row in resread:
			if(row[0] != 'None'):
				chosenpep = row[0]
				candidatepep = ast.literal_eval(row[2])
				scan = row[3]
				# print(scan)
				resultpeps.append([scan,chosenpep,candidatepep])
	return resultpeps

def main():
	test_scanpeps,dict_testscanpeps = parseTestFile()
	result_peps = parseResultsFile()

	for result in resultpeps


if __name__ == "__main__":
	main()