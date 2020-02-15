# ordinal numbers replacement

def numberOrdinal(number) :
    ''' A function that takes a number and returns the orinal number replacement'''

    if number == 0 :
        return '0'
  
    # define a dictinary
    dictDigits = {1 : "st", 2 : "nd", 3 : "rd"}
  
    # last digit
    nString1 = str(number)[-1]
    N1 = int(nString1)
  
    # last 2 digits
    nString2 = str(number)[-2:]
    N2 = int(nString2)
  
    if N2 >= 10 and N2 <= 19 :
        return str(number) + "th"
    elif N1 >=1 and N1 <= 3 :
        return str(number) + dictDigits[N1]
    else :
        return str(number) + "th"

# give a number
n = 12353
print(numberOrdinal(n))
