# given a list of integers, print the duplicates

def findDuplicates(aList) :
	''' a function that gets a list of integers and removes the duplicates'''
	
	# initialize a dictinary with keys the number of the list, and values the 
	# number of occurences
	seen = {}
	
	# initalize a list for the duplicates
	duplicates = []
	
	for elem in aList :
		if elem not in seen :
			seen[elem] = 1
		else :
			if seen[elem] == 1 :
				duplicates.append(elem)
		
			seen[elem] += 1

	return duplicates

# main program

# define a list of integers
aList = [1, 2, 2, 4, 5, 5, 2, 1, 4, 7]

# print the duplicate numbers
print(findDuplicates(aList))
