  

x = raw_input()

while( x!= "#"):
    
    x = x.split()
    N = int(x[0])
    B = int(x[1])

    cowdetails = []
    #Has tuples of (P_i, Sum)
    
    for i in range(N):
        x1 = raw_input()
        x1 = x1.split()
        cowdetails.append((int(x1[0]),int(x1[0])+int(x1[1])))
    
    cowdetails = sorted(cowdetails, cmp=lambda x,y: x[1]-y[1])
    #sorted by sum
    
    counter = 0
    i = 0
    gifts = 0
    while (counter + cowdetails[i][1]) <= B and i<len(cowdetails):
        counter += cowdetails[i][1]
        gifts += 1
        i += 1

    #now we stopped at cow where sum exceeded budget!
    Psort = sorted(cowdetails[0:i+1], cmp=lambda x,y: x[0]-y[0])

    saving = Psort[i][0]/2
    
    if ((counter-saving) + cowdetails[i][1]) <= B:
        print gifts+1
    else:
        print gifts

    x = raw_input()

