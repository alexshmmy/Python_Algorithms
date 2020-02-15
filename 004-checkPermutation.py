# time complexity: O(n)
# space complexity: O(1)
# We define a permutation as a rearrangement of characters i.e. two strings
# that are permutations of each other must contain exactly the same characters with the
# same frequency.

def checkPermutation(String1, String2) :
	'''A function that checks if two strings are permutation to each other'''

	if len(String1) != len(String2) :
		return False
	
	# define a bit vector with all entries 0s
	bit_vector = [False]*128

	for character in String1 :
		idx = ord(character)
		bit_vector[idx] = not bit_vector[idx]

	for character in String2 :
		idx = ord(character)
		bit_vector[idx] = not bit_vector[idx]

	# if the strings are permutation to each other
	# the bit_vector will contain only False entries
	# otherwise it will contain at least a True entry

	return sum(bit_vector) == 0

# main program
print(checkPermutation.__doc__)
String1 = 'geeksforgeeaks'
String2 = 'forgeeksgeeks'

#print(checkPermutation(String1, String2))

if checkPermutation(String1, String2) :
	print("'%s' is a permutation of '%s'" % (String1, String2))
else :
	print("'%s' is not a permutation of '%s'" % (String1, String2))
