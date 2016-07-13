def getlast(x):
    for i in range(len(x)-1, -1, -1):
        if x[i] == "F":
            return i
    return -1


def getF(s,P,x,y):
    xdiff = x
    ydiff = y

    for i in range(len(s)):
        if s[i] == "F":
            P[1] += 1*ydiff
            P[0] += 1*xdiff

        elif s[i] == "L":
            temp = ydiff
            if ydiff == 0:
                if xdiff == 1:
                    ydiff = 1
                else:
                    ydiff = -1
            else:
                ydiff = 0

            if xdiff == 0:
                if temp == 1:
                    xdiff = -1
                else:
                    xdiff = 1
            else:
                xdiff = 0

        else:
            temp = ydiff
            if ydiff == 0:
                if xdiff == 1:
                    ydiff = -1
                else:
                    ydiff = 1
            else:
                ydiff = 0

            if xdiff == 0:
                if temp == 1:
                    xdiff = 1
                else:
                    xdiff = -1
            else:
                xdiff = 0

    return (P[0],P[1])



x = raw_input()
while( x!= "#"):
    # x is the command string.
    finalPs = [] #final positions

    L = len(x)
    
    P = [0,0]
     #north
    xdiff = 0
    ydiff = 1

    for i in range(L):
        cmd = x[i]
        restofS = x[i+1:]
        if cmd == "L":
            one = "R" + restofS
            two = "F" + restofS
        elif cmd == "R":
            one = "L" + restofS
            two = "F" + restofS
        else:
            one = "R" + restofS
            two = "L" + restofS

        finalPs.append(getF(one,P[:], xdiff, ydiff))
        finalPs.append(getF(two,P[:], xdiff, ydiff))
            
        if cmd == "F":
            P[1] += 1*ydiff
            P[0] += 1*xdiff
        elif cmd == "L":
            temp = ydiff
            if ydiff == 0:
                if xdiff == 1:
                    ydiff = 1
                else:
                    ydiff = -1
            else:
                ydiff = 0
            if xdiff == 0:
                if temp == 1:
                    xdiff = -1
                else:
                    xdiff = 1
            else:
                xdiff = 0
        else:
            temp = ydiff
            if ydiff == 0:
                if xdiff == 1:
                    ydiff = -1
                else:
                    ydiff = 1
            else:
                ydiff = 0
            if xdiff == 0:
                if temp == 1:
                    xdiff = 1
                else:
                    xdiff = -1
            else:
                xdiff = 0


    print len(set(finalPs))
    x = raw_input()

    
