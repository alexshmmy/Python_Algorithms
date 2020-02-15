# time complexity: O(n)
# space complexity: O(n)

def StringCompression(string) :
	''' A function that takes a string and writes it back compressed'''
	''' Input: aabccccaaa, Output: a2b1c3a3''' 
	
	# compute the length of the string
	lenString = len(string)

	# if the given string is empty, return empty string ''	
	if lenString == 0 :
		return ''

	# set compressed in the begining of the string
	compressed = string[0]

	# save the number of repetitive characters
	num_dupes = 1

	# iterate over the rest of the string
	for i in range(1, lenString) :
		if string[i] == string[i-1] :
			num_dupes += 1
		else:
			compressed += str(num_dupes) + string[i]
			num_dupes = 1
	
	compressed += str(num_dupes)
	
	# convert back the list to string
	return ''.join(str(x) for x in compressed)

# main program
print(StringCompression.__doc__)

# give a string
#String = 'aabccccccccccaaaaaaa'
String = 'abbceeeeeefww'

# print the result to the screen
print("Intput: %s, Output: %s" % (String, StringCompression(String)))
