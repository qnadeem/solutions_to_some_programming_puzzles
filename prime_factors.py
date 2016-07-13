import math

def isP(x):
    if(x<2):
        return False
    root = int(round(math.sqrt(x)))+1

    for i in  range(2,root):
        if (x%i==0):
            return False
    return True

c = 600851475143


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors


pfs = prime_factors(c)

print max(pfs)



