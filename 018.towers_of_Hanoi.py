from datetime import datetime

# start counting the time
start_time = datetime.now()

def move(frm, to) :
    print('move from ', frm, 'to ', to)

def towers(n, frm, to, spare) :
    if (n == 1) :
    	move(frm, to)
    else :
    	towers(n-1, frm, spare, to)
    	towers(1, frm, to, spare)
    	towers(n-1, spare, to, frm)

# main program

# run the towers function
towers(15, 'A', 'B', 'C')

# stop counting the time
end_time = datetime.now()

# print the time duration
print('Duration: {}'.format(end_time - start_time))
