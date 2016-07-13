def getstring(small,s):
    for i in range(len(small)-1,-1,-1):
        addition = min(s, 9-int(small[i]))
        small = small[:i]+str(int(small[i])+addition)+small[i+1:]
        s -= addition
        if s==0:
            return small
    return -1
    
def getsstring(small,s):
    for i in range(0,len(small)):
        addition = min(s, 9-int(small[i]))
        small = small[:i]+str(int(small[i])+addition)+small[i+1:]
        s -= addition
        if s==0:
            return small
    return -1
    
x = raw_input()
x = x.split()

m = int(x[0])
s = int(x[1])

if s==0:
    if m>1:
        print -1,-1
    else:
        print 0, 0

else: # find smallest of length m. and sum s.
    if s > m*9:
        print -1,-1
    else:
        small = "1"
        for i in range(m-1):
            small += "0"
        s = s-1 # a 1 has been used.

        SMALL = getstring(small,s)

        BIG = getsstring(small,s)

        print SMALL,BIG
        


