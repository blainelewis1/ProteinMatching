#!/usr/bin/env python
# @author mathew teoh
import csv 
import ast

def parseTestFile():
	testscanpeps = {}
	# size = 0
	with open('commercial.csv','rt') as csvfile:
		testread = csv.reader(csvfile,delimiter=',')
		next(testread)
		for row in testread:
			testpeptide = remove_dat_hoohah(row[0])
			scannum = row[6]
			testscanpeps[scannum] = testpeptide
			# print(testpeptide)

	return testscanpeps

def remove_dat_hoohah(testpeptide):
	return testpeptide.replace("(+57.02)","")

def parseResultsFile():
	resultpeps = {}
	with open('result.tsv','rt') as csvfile:
		resread = csv.reader(csvfile,delimiter='\t')
		for row in resread:
			if(row[0] != 'None'):
				chosenpep = row[0]
				candidatepep = ast.literal_eval(row[2])
				scan = row[3]
				resultpeps[scan] = [chosenpep,candidatepep]

	return resultpeps

def main():
	test_scanpeps = parseTestFile() # e.g. ['399', 'CCAAADPHECYAK']
	result_peps = parseResultsFile() # e.g. ['521', 'TK', ['TK']]

	count = 0
	for result in result_peps:
		# false positives
		if(result_peps[result][0] != test_scanpeps.get(result,None)):
			count += 1
			print(count,result,result_peps[result],test_scanpeps.get(result,None))
	for scans in test_scanpeps:
		# false negatives
		if(result_peps.get(scans,None) == None):
			count += 1
			print(count,test_scanpeps.get(scans,None))



if __name__ == "__main__":
	main()