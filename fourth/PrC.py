def addtoeachlist(e, L):
    # e number
    #L is list of lists. add e to each list.
    for i in L:
        i.append(e)
    return L
def powerset(C):
    if C == []:
        return [[]]
    else:
        return powerset(C[1:]) + addtoeachlist(C[0],powerset(C[1:]))
        
def maxL(l):
    ans = 0
    for i in l:
        if len(i) > ans:
            ans = len(i)
    return ans

#check if group works
def nocarry(L):
    #L sorted. last element has highest digits.
    lenn = maxL(L)
    for i in range(lenn):
        counter = 0
        for x in range(len(L)):
            t = len(L[x])

            if (t > i):
                counter = counter + int(L[x][t-1-i])

            if counter >= 10:
                return False
    return True

    




    
  

x = raw_input()

while( x!= "#"):
    
    N = int(x) # number of cows.

    CW = []
    #Has tuples of (g_i, d_i)
    
    for i in range(N):
        x1 = raw_input()
        CW.append(x1)

    PS = powerset(CW)
    maxx = 0

    for i in PS:
        worked = nocarry(i)
        if worked == True:
            if len(i) >= maxx:
                maxx = len(i)
        

    print maxx

    x = raw_input()

