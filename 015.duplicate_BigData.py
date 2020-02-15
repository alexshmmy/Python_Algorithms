# given a big .csv file that does not fit in the RAM, remove duplicate lines

import hashlib

with open('input.csv', 'r') as file_in, open('output.csv', 'w') as file_out :
	# a set to hold visited lines
	visited_rows = set()
	
	# iterate over the rows of the 'input.csv' file
	for row in file_in :
		# hash the value
		row_hash = hashlib.md5(row.encode()).digest()
		
		if row_hash not in visited_rows :
			# this row is visited first time
			
			# add the row to the hash table
			visited_rows.add(row_hash)
			
			# write the line to the output
			file_out.write(row)
