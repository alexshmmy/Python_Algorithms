# time complexity : O(n)
# space complexity : O(1)

def palindromePermutation(string) :
	''' A function that checks if a given string is a permutation of a'''
	''' palindrome string'''
	
	# define a bit vector for ASCII characters
	bit_vector = [False] * 128
	
	# count the number of non-space characters	
	num_valid_chars = 0
	
	# traverse the string one character per time
	for character in string :
		# save the ASCII number of the character
		idx = ord(character)
		# if character is a non-space
		if idx >= 0 and idx <= 127 and character != ' ' :
			num_valid_chars += 1
			bit_vector[idx] = not bit_vector[idx]

	# if the input string without spaces has even length and the sum of
	# the bit_vector is 0, then the string is palindrome permutation
	if num_valid_chars % 2 == 0 :
		return sum(bit_vector) == 0
	
	# if the inpust string without spaces has odd length and the sum of
	# the bit_vector is 1, then the string is palindrome permutation
	return sum(bit_vector) == 1

# main program
print(palindromePermutation.__doc__)

# define a string
string = 'tact coa'

if palindromePermutation(string) :
	print("The string '%s' is a palindrome permutation!" % string)
else :
	print("The string '%s' is not a palindrome permutation!" % string)
