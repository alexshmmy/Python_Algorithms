# given a 2D array and a word, build a boolean function that checks if the word is in the 
# array horizontally or vertically

# import packages
import numpy as np

# basic function
def findWord2DArray(array, word) :
	'''gets an array and a word and checks if the word exists in the array'''
	
	# define the length of the array
	rows, columns = array.shape

	# compute the length of the word
	L = len(word)

	# check if the length of the word is smaller than the smallest dimension
	# of the array or the word is empty
	if min(rows, columns) < L or L == 0 :
		return False

	# if the word has 2 or more characters, scan the array
	for i in range(rows) :
		for j in range(columns) :
			# check horizontally
			# k is an index parsing the word					
			k = 0
			while (k <= L-1) :
				# if the character is same with the word increase k
				if j+k <= columns-1 and array[i, j+k] == word[k] :
					k += 1
				else :
					break
							
			if k == L and array[i, j+k-1] == word[-1] :
				return True						
							
			# same procedure vertically
			k = 0
			while (k <= L-1) :
				if i+k <= rows -1 and array[i+k, j] == word[k] :
					k += 1
				else :
					break					
			
			if k == L and array[i+k-1, j] == word[-1]:
				return True

	# after parsing the matrix, the word is not found
	return False

# main program
# define a word
word = 'q1fvd'

# define an 2D array of characters
array = np.array([['a', 'q', 'u', 'q', 'a'], 
					['b', '1', 'd', '1', 'a'],
					['b', 'f', 'f', 'f', 'a'], 
					['a', 'x', 'l', 'v', 'a'],
					['a', 'b', '1', 'd', 'a']])

# check if the word exists in the 2D array
if findWord2DArray(array, word) :
	print('The word exists in the 2D array!')
else :
	print('The word does not exist in the 2D array!')
