# input: a 2D matrix
# output: checks if the matrix is identity matrix
# complexity: O(n^2)

import time
import numpy as np

# function
def checkArray(arr):
	''' Checks if a given 2D array is the identity'''	
	
	# compute the length of the array
	n = len(arr)

	# iterate over the array
	for i in range(n):
		for j in range(n):
			if i == j and arr[i,j] != 1 :
				return False
			elif i != j and arr[i,j] != 0 :
				return False

	# all the checks are done. The matrix is identity.
	return True
 
# main program
start = time.time()
# arr = np.array([[1,0,0], [0, 1, 0], [0, 1, 1]])
n = 100
arr = np.identity(n)

if checkArray(arr) :
	print("The given matrxix is the identity matrix")
else :
	print("The given matrix is not identity!")

end = time.time()
t = end-start
print("The execution time is : %.3f seconds" % t)
