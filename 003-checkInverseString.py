# time complexity: O(n)
# space complexity: O(1)

def checkInverseStrings(String1, String2) :
	'''A function that checks if two strings are inverse to each other'''

	if len(String1) != len(String2) :
		return False
	else :
		for i in range(0, len(String1)) :
			if String1[i] != String2[-i-1] :
				return False

	return True	

# main program
print(checkInverseStrings.__doc__)
String1 = 'abcdefghijk1'
String2 = '1kjihgfedcba'

if checkInverseStrings(String1, String2) :
	print("'%s' is inverse of '%s'" % (String1, String2))
else :
	print("'%s' is not inverse of '%s'" % (String1, String2))
