import math


x = raw_input()
while( x!= "#"):
    n = int(x)
    H = []
    for i in range(n):
        H.append(int(raw_input()))
    H.sort()
    # H is a sorted hill.
    costs = []

    for i in range(0,83):
        cost = 0
        for x in range(n):
            h = H[x]
            if h < i:
                cost += (i-h)**2
            elif h > i+17:
                cost += (h - (i+17))**2
        costs.append(cost)
        
    print min(costs)

    x = raw_input()

    
