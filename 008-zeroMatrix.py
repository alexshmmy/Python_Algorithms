# import packages
import numpy as np

def zeroMatrix(array) :
	'''A function that takes a N x M array and puts replaces every zero element'''
	'''with the corresponding zero row and column'''
	
	# time complexity: O(NxM)
	# space complexity: O(NxM)
	
	# compute the dimensions of the array
	rows, columns = np.shape(array)
	
	# indicator matrix
	temp = np.array(array == 0)
	
	for i in range(rows) :
		for j in range(columns) :
			if temp[i][j] == True :
				# make row i zero
				array[i, :] = 0

				# make column j zero
				array[:, j] = 0
	
	# return the modified array
	return array

def zeroMatrix2(array) :
	'''A function that takes a N x M array and puts replaces every zero element'''
	'''with the corresponding zero row and column'''
	
	# time complexity: O(NxM)
	# space complexity: O(1)
	
	# compute the dimensions of the array
	rows, columns = np.shape(array)
	
	# check if first row has zeros
	first_zero_row = False
	for j in range(columns) :
		if array[0][j] == 0 :
			first_zero_row = True
			break

	# check if first column has zeros
	first_column_zero = False
	for i in range(rows) :
		if array[i][0] == 0 :
			first_column_zero = True
			break

	# check the rest of the matrix for zeros and use the first row and column 
	# to store the information
	for i in range(1, rows) :
		for j in range(1, columns) :
			if array[i, j] == 0 :
				array[0, j] = 0
				array[i, 0] = 0		

	# look at storage and apply zeros to approapriate rows and columns
	for i in range(1, rows) :
		if array[i, 0] == 0 :
			array[i, :] = 0

	for j in range(1, columns) :
		if array[0, j] == 0 :
			array[:, j] = 0

	# look the first row/column
	if first_zero_row :
		array[0, :] = 0
	if first_column_zero :
		array[:, 0] = 0
	
	# return the modified array
	return array

# main program
print(zeroMatrix.__doc__)

# define a NxM matrix
array1 = np.array([[1, 1, 3, 4, 2], [3, 4, 5, 0, -1], [6, 7, -10, 9, 8], [1, 1, 2, 3, 5], [1, 1, 1, 1, 0]])

array2 = np.array([[1, 1, 3, 4, 2], [3, 4, 5, 0, -1], [6, 7, -10, 9, 8], [1, 1, 2, 3, 5], [1, 1, 1, 1, 0]])

# print the array
print("\n")
print("Given array: ")
print(np.matrix(array1))

# print the modified array with method 1
print("\n")
print("Modified array: ")
print(np.matrix(zeroMatrix(array1)))

# print the modified array with method 2
print("\n")
print("Modified array: ")
print(np.matrix(zeroMatrix2(array2)))
