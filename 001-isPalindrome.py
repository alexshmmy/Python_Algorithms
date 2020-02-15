# time complexity : O(n)
# space complexity : O(1)

'''This module deals with palindrome strings'''

def isPalindrome(String) :
	'''A function that takes a string and checks if it is palindrome'''

	L = len(String) // 2
	for i in range(0, L) :
		if String[i] != String[-i-1] :
			return False
	
	return True

# main program
print(isPalindrome.__doc__)
String = 'alexxela'
#String = 'abab'
#String = 'ab12ba'

if isPalindrome(String) :
	print("The string '%s' is palindrome!" % String)
else :
	print("The string '%s' is not palindrome!" % String)
