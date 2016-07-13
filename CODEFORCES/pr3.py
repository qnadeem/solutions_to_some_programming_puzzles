import math

def highestpptwo(l,r):#highest power of 2 less than or equal to r+1
    count = 0
    r+=1
    while(r>0):
        r = r/2
        count+=1

    res = 2**(count-1)-1
    if(res>=l):
        return res
        
    else:
        return -1



n= int(raw_input())

ans =[]

for i in range(n):
    x = raw_input()
    x = x.split()

    l = int(x[0])
    r = int(x[1])


    ans = highestpptwo(l,r)

    if ans != -1:
        print ans

    else:
        maxx = 0
        res = l
        for i in range(l,r+1):
            ones = bin(i)[2:].count("1")
            if ones>maxx:
                maxx = ones
                res = i

        print res

    



    
