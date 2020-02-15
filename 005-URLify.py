# time complexity: O(n)

def URLify(string) :
	'''A function that gets a string and repaces the space characters with '%20' '''
	
	# compute the length of the given string
	L = len(string)

	# define an empty new list
	newString = []
	
	# define an index for positioning the list newString
	idx = 0

	for i in range(0, L) :
		if string[i] == ' ' :
			newString.append('%20')
			idx += 3
		else :
			newString.append(string[i])
			idx += 1
	# convert the list to string
	return ''.join(str(x) for x in newString)

def URLify2(string) :
	'''A function that gets a string and repaces the space characters with '%20' '''
	
	# compute the length of the given string
	L = len(string)

	# define an empty new string
	newString = ''

	for i in range(0, L) :
		if string[i] == ' ' :
			newString += '%20'
		else :
			newString += string[i]

	# convert the list to string
	return newString		

def URLify_InPlace(string) :
	'''A function that gets a string and repaces the space characters with '%20' '''
	''' In-place algorithm implementation'''

	# convert the string to list of characters
	string = list(string)
	
	# new_len stands for the number of spaces
	new_len = 0
	
	# reader is the index at the end of un-extended string
	reader = len(string)-1

	# count the number of spaces
	for character in string :
		if character == ' ' :
			new_len += 3	
		else :
			new_len += 1
	
	# extend the length of the string to fit the URL
	string += [' ']*(new_len - len(string))
	
	# writer is an index at the end of the extended string
	writer = len(string)-1
	
	while reader >= 0 and writer >= 0 :
		if string[reader] == ' ' :
			string[writer] = '0'
			string[writer - 1] = '2'
			string[writer -2] = '%'
			reader -= 1
			writer -= 3
		else :
			string[writer] = string[reader]
			reader -= 1
			writer -= 1
	
	# convert the list back to string
	return ''.join(str(x) for x in string)

# main program

# print the function doc
print(URLify.__doc__)
print(URLify2.__doc__)
print(URLify_InPlace.__doc__)

# define a string
string = ' a le  x  '

# run the functions
print("Initial string : '%s' " % string)
print('Final string : ', URLify(string))
print('Final string : ', URLify2(string))
print('Final string : ', URLify_InPlace(string))
