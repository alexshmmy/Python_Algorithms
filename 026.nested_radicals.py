# computation of sequenses of nested radicals
#
# 3 type of sequences:
# Type 1: (positive sign)
# sqrt(n+sqrt(n+sqrt(n+...)))
#
# Type 2: (negative sign)
# sqrt(n-sqrt(n-sqrt(n-...)))
#
# Type 3: (alternating sign)
# sqrt(n-sqrt(n+sqrt(n-...)))

import math

def nestedRadical(n, N, Sign):
    # i denotes the time a sqare root is computed
    i = 1 
    # compute the first square root
    t = math.sqrt(n)

    if Sign == "+":
        while i <= N:
            t = math.sqrt(n+t)
            i = i+1
    elif Sign == "-":
        while i <= N:
            t = math.sqrt(n-t)
            i = i+1
    elif Sign == 0:
        while i < N:
            if N % 2 == 0:
                y = (-1)**i
                t = math.sqrt(n+y*t)
                i = i+1
            else:
                y = (-1)**(i+1)
                t = math.sqrt(n+y*t)
                i = i+1
    return t

if __name__ == "__main__":
    # define a number n > 0
    n = 15

    # number of iterations for precision
    N = 100

    ##### positive nested radical sequence
    # computed by forula
    print(0.5*(math.sqrt(4*n+1)+1))
    # computed numerically
    print(nestedRadical(n, N, "+"))

    ##### negative nested radical sequence
    # computed by formula
    print(0.5*(math.sqrt(4*n+1)-1))
    # computed numerically
    print(nestedRadical(n, N, "-"))

    ##### alternating sign nested radical sequence
    # computed by formula
    print(0.5*(math.sqrt(4*n-3)-1))
    # computed numerically
    print(nestedRadical(n, N, 0))