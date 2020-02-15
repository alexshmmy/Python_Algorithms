# time complexity best: O(nlog(n))
# time complexity worst: O(n^2)
# space complexity: O(1)

def quickSort(arr) :
	''' implementation of classical Quicksort algorithm'''

	if len(arr) <= 1 :
		return arr
	
	# compute the pivot
	pivot = arr[len(arr) // 2]
	
	# compute the left, middle and right lists
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]

	# return the result recursively
	return(quicksort(left) + middle + quicksort(right))

# main program

# define an list of integers to be sorted
arr = [54, 26, -5, 93, 17, -1, 77, 31, 44, 55, 20]

# print the results
print('Initial list : \n', arr)
print('Sorted list : \n', quickSort(arr))
