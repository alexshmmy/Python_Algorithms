# bublesort: a basic sorting algorithm in python
# input: a list of integers
# output: sorted list of integers
# time complexity: O(n^2)
# space complexity: O(1)

def bubbleSort(alist) :
	'''implementation of bubblesort algorithm'''

	# compute the length of the list
	L = len(alist)
	for i in range(0, L) :
		for j in range(0, L-i-1) :
			if alist[j] > alist[j+1] :
				alist[j], alist[j+1] = alist[j+1], alist[j]

# main program
alist = [54,26,100,93,-5,17,77,31,44,55,-1,-100]
bubbleSort(alist)
print(alist)
