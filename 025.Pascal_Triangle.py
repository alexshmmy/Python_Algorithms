# input: an integer n > 1
# output: the Pascal's triangle of order n
# comlexity:  O(n^2)

import numpy as np

# function for pascal triangles
def pascalTriangle(n):
	''' Computes the Pascal's Triangle for a number n > 1'''

	# initialize an nxn matricx of zeros
	arr = np.zeros((n, n))

	# iterate over the lines
	for line in range(n):
		#iterate over the columns
		for j in range(line+1):
			if j == 0 or line == j:
				arr[line, j] = 1
			else:
				arr[line, j] = arr[line-1,j-1]+arr[line-1,j]

	# return the array
	return arr

# main program
n = 12
print(pascalTriangle(n))
