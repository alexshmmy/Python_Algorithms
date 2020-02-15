# Integer solutions of the equation: a^3+b^3 = c^3+d^3
# Time complexity O(n^2)

def integerSolutions(n) :
    # initialize a dictionary for hashing
    dictHash = {}
    
    for c in range(n+1):
    	for d in range(n+1):
    		result = c**3+d**3
    		dictHash[result] = (c, d)
    
    for a in range(n+1):
    	for b in range(n+1):
    		result = a**3+b**3
    		
    		if result in dictHash.keys():
    			(c, d) = dictHash[result]
    			print("(a, b, c, d) = (%d, %d, %d, %d)" % (a, b, c, d))

# main program

# upper bound of integers
n = 5

# print the integer solutions
integerSolutions(n)
