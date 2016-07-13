def simulate(B, E, bsize, esize):
    meets = 0
    
    b = 0
    e = 0  #Starting positions

    bprev = 0
    eprev = 0#positions 1 time ago.


    while (not(bsize==0 and esize==0)):
        #go forward 1 time..
        if (bsize!=0 and B[0] == 0):
            B = B[1:]
            bsize-=1
            if bsize ==0:#prev move was LAST!
                bprev = b
                
        if (esize!=0 and E[0] == 0):
            E = E[1:]
            esize-=1  #check if first clause finished.
            if esize ==0:#prev move was LAST!
                eprev = e
            

        if(bsize !=0): #B. has moves, and not 0. move B.
            if B[0] < 0:
                b = b-1
                bprev = b+1
                B[0] = B[0] + 1
            elif B[0] >0:
                b = b+1
                bprev = b-1
                B[0] = B[0] - 1

        if(esize != 0):#E. has moves, and not 0. move E.
            if E[0] < 0:
                e = e-1
                eprev = e+1
                E[0] = E[0] + 1
            elif E[0] >0:
                e = e+1
                eprev = e-1
                E[0] = E[0] - 1


        if ((e==b) and (eprev!=bprev)):
            meets = meets+1

    return meets



def getmoves(array, x):
    for i in range(x):
        e = raw_input()
        e = e.split()
        dist = int(e[0])

        if e[1]=="L":
            dist = (-1)*dist
        array.append(dist) 


x = raw_input()

while( x!= "#"):
    
    BnE = str(x) #how many moves in the following dance challenge.
    commands = BnE.split()
    B = int(commands[0])
    E = int(commands[1])


    Bmoves = []   #arrays to hold moves
    Emoves = []

    getmoves(Bmoves, B)
    getmoves(Emoves, E) #add all moves to the arrays and then work!

    MEETS = simulate(Bmoves, Emoves, B, E)  # SIMULATE COW movements.
    print MEETS

    x = raw_input()

