def checkE(x,separate, start, done):
    relation = 0

    BLx = x[0]
    BLy = x[1]
    TRx = x[2]
    TRy = x[3]

    for i in range(start, len(separate)):
        t = separate[i]
        BLix = t[0]
        BLiy = t[1]
        TRix = t[2]
        TRiy = t[3]

        #if x enclosed inside i
        if done==0 and BLx >= BLix and BLy >= BLiy and TRx <= TRix and TRy<= TRiy:
            return

        # if i enclosed in x.
        elif BLx <= BLix and BLy <= BLiy and TRx >= TRix and TRy>= TRoy:
             separate = separate[:i] + [x] + separate[i+1:]
             checkE(x,separate,i+1,1)

    if done==0:
        separate.append(x)

def getenclosures(AC, separate):
    for i in AC:
        checkE(i,separate,0,0)
    

x = str(raw_input())

while( x!= "#"):
    number = int(x)
    allcoord = []


    for i in range(number):
        x = raw_input()
        x = x.split()
        allcoord.append([int(x[0]),int(x[1]),int(x[2]),int(x[3])])

    separate = []
    getenclosures(allcoord, separate)
    print len(separate)

    x = raw_input()
