# Time complexity O(n)
# Space complexity O(1)

def isUnique(String) :
	'''A function that checks if a string has unique characters'''
	
	# define a hash table of all ASCII codes
	hash_table = [False] * 128

	for character in String :
		idx = ord(character)
		
		if hash_table[idx] == True :
			return False
		
		hash_table[idx] = True
	
	return True

# main program
print(isUnique.__doc__)

# define a string to check
String = 'abcdefghijklmnopqrstuvwxyz!~@#$%^&*(a'

if isUnique(String) :
	print("The string '%s' has unique characters!" % String)
else :
	print("The string '%s' has not unique characters!" % String)
