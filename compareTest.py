#!/usr/bin/env python
# @author mathew teoh
import csv 

def parseTestFile():
	testscanpeps = []
	with open('commercial.csv','rt') as csvfile:
		testread = csv.reader(csvfile,delimiter=',')
		next(testread)
		for row in testread:
			# print(row)
			# print(row[0])
			testpeptide = remove_dat_hoohah(row[0])
			scannum = row[6]
			# print(testpeptide)
			# print(scannum)
			testscanpeps.append([scannum,testpeptide])
	return testscanpeps

def remove_dat_hoohah(testpeptide):
	return testpeptide.replace("(+57.02)","")

def parseResultsFile():
	resultpeps = []
	with open('results.csv','rt') as csvfile:
		resread = csv.reader(csvfile,delimiter='\t')
		for row in resread:
			if(row[0] != 'None'):
				chosenpep = row[0]
				candidatepep = row[2]
				print(candidatepep)

def main():
	test_scanpeps = parseTestFile()
	parseResultsFile()


if __name__ == "__main__":
	main()