# input: a sorted list, an integer
# output: returns True if the integer is on the list, False otherwise
# time complexity: O(log(n))
# space complexity: O(1)

def binarySearch(alist, item) :
	'''Iplementation of binary search'''
	
	first = 0
	last = len(alist)-1

	while first <= last :
		mid = (first + last) // 2
		if alist[mid] == item :
			return True	
		elif item < alist[mid] :
			last = mid-1
		else :
			first = mid+1
	
	return False
	
# main program

# give a test list
testlist = [-120, -10, 0, 1, 5, 15, 50, 80, 91, 98, 100]

# print the result
print(binarySearch(testlist, 1))
print(binarySearch(testlist, -5))
