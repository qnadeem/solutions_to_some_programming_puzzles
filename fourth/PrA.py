def getans(CD, N):

    totalM = 0 #milk
    timesD = [] #time slots filled

    dontwork = 0

    for y in range(N):
        
        d_i = CD[y][1]
        
        if d_i not in timesD:
            #deadline time available!
            timesD.append(d_i)
            totalM += CD[y][0]
        
        elif d_i > dontwork:
            #deadline time is not open!

            od = d_i - 1
            worked = False
            
            while od >= 1 and od > dontwork:
                if od not in timesD:
                    timesD.append(od)
                    totalM += CD[y][0]
                    worked = True
                    od = -1
                
                od = od - 1

            if worked == False:
                if d_i > dontwork:
                    dontwork = d_i
    return totalM
    

x = raw_input()

while(x!= "#"):   
    N = int(x) # number of cows.

    CD = []
    #Has tuples of (g_i, d_i)
    
    for i in range(N):
        x1 = raw_input()
        x1 = x1.split()
        CD.append((int(x1[0]),int(x1[1])))  

    CD = sorted(CD, cmp=lambda x,y: y[0]-x[0])
    #sorted by g_i, meaning the gallons

    totalM = getans(CD, N)   

    print totalM
    x = raw_input()

