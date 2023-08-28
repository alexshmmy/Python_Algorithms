# A prime number is called unidigital prime, if all its digits are used once. 
# Write an efficient program that computes if a given number is unidigital prime

import math

def is_prime(n: int) -> bool: 
    # Check if n=1 or n=0
    if n <= 1:
        return False
     
    # Check if n=2 or n=3
    if n == 2 or n == 3:
        return True
     
    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
     
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    for i in range(5, int(math.sqrt(n))+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
 
    return True

def is_unidigital_prime(num: int) -> bool:
    # Convert the number to a string and check if it has repeated digits
    digits = str(num)
    if len(digits) != len(set(digits)):
        return False
    
    # Check if the number is prime
    if is_prime(num):
        return True 
    else:
        return False

if __name__ == "__main__":
    n = 4321
    print(f"Is {n} unique digit prime? {is_unidigital_prime(n)}")
