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

def parseResultsFile(filename):
	resultpeps = {}
	with open(filename,'rt') as csvfile:
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
	
	test_filename = 'result.tsv'#'big_results.tsv'
	result_peps = parseResultsFile(test_filename) # e.g. ['521', 'TK', ['TK']]

	count_correct = 0
	count_fp_nones = 0
	count_fp_mismatch = 0
	count_fn = 0
	for result in result_peps:
		if(result_peps[result][0] == test_scanpeps.get(result,None)):
			count_correct = count_correct + 1
		else:
			if(test_scanpeps.get(result,None) == None):
				count_fp_nones = count_fp_nones + 1
			else:
				count_fp_mismatch = count_fp_mismatch + 1
				print(count_correct,result,result_peps[result],test_scanpeps.get(result,None))
	for scan in test_scanpeps:
		if(result_peps.get(scan,None) == None):
			count_fn = count_fn + 1


	print('Number we got right: %d', count_correct)
	print('Number we got, test has none: %d', count_fp_nones)
	print('Number we got, test has different: %d', count_fp_mismatch)
	print('Number we aint got, test has: %d', count_fn)
	print('Number total in test data: %d', len(test_scanpeps))
	# 	# false positives
	# 	if(result_peps[result][0] != test_scanpeps.get(result,None)):
	# 		count += 1
	# 		print(count,result,result_peps[result],test_scanpeps.get(result,None))
	# for scans in test_scanpeps:
	# 	# false negatives
	# 	if(result_peps.get(scans,None) == None):
	# 		count += 1
	# 		print(count,test_scanpeps.get(scans,None))



if __name__ == "__main__":
	main()