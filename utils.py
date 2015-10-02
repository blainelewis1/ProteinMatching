import math

def binary_error_search(data, item, error):

	left = 0
	right = len(data)
	cur = 0

	while(left <= right):

		cur = (right + left)//2

		if(item > data[cur]):
			left = cur + 1
		elif(item < data[cur]):
			right = cur - 1
		else:
			break

	matches = []

	#print(cur, data[cur], item)

	#sequential search left
	i = cur
	while(i < len(data) and data[i] <= item + error):
		if data[i] >= item - error:				
			matches.append(data[i])
		i += 1

	#sequential search right
	i = cur - 1
	while(i >= 0 and data[i] >= item - error):
		if data[i] >= item - error:
			matches.append(data[i])
		i -= 1

	#for match in matches:
	#	print(match, "<=", item + error,  "and", match ,">=", item - error)
	#	assert(match <= item + error and match >= item - error)

	return matches	


def normalize_data(data):
	max_value = max(data, key = lambda item: item[1])[1]
	
	return [(item[0], item[1]/max_value) for item in data]