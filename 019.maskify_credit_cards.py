# Usually when you buy something, you're asked whether your credit card number, 
# phone number or answer to your most secret question is still correct. However, 
# since someone could look over your shoulder, you don't want that shown on your 
# screen. Instead, we mask it. Your task is to write a function maskify, which 
# changes all except the first character and the last four characters into '#'.

def maskify(credit_card) :
    if len(credit_card) < 6 :
        return credit_card
  
    output = credit_card[0]
  
    for x in credit_card[1:-4] :
        if x.isdigit() :
            output += "#"
        else :
            output += x
  
    output += credit_card[-4:]
  
    return output
  
# main program
cc = "4444-2^45-4%56-7777"
print(maskify(cc))
