
x = raw_input()

while( x!= "#"):
    x = x.split()

    N = int(x[0])
    A = int(x[1])
    B = int(x[2])

    pos = []

    for i in range(N):
        x = raw_input()
        pos.append(int(x))

    pos.sort()


    cost = 0
    index = 0 #till N

    WIFI = []

    while index != N:
        atcow = index

        if atcow+1 == N: #at end..
            cost += A
            index += 1

            #print "WiFi at " + str(pos[atcow]) + "because last cow"

        else:
            # first check if can NOT install wifi between the cows. that is separate on point wifis for the first cow.
            midcost = ((pos[atcow+1]-pos[atcow])/2.0)*B
            if midcost >= A:
                cost += A
                index += 1
                #print "WiFi at " + str(pos[atcow]) + "because midcost is >= A"

            else: # should install wifi between these 2, or these 3, or these 4 etc..
                prevmidcost = midcost
                
                endcow = atcow+1
                midcost = ((pos[endcow]-pos[atcow])/2.0)*B

                while midcost < prevmidcost+A and (endcow < N-1):
                    endcow += 1
                    prevmidcost = midcost
                    midcost = ((pos[endcow]-pos[atcow])/2.0)*B

                if endcow< N-1:
                    # make wifi between all these cows.

                    midcost = ((pos[endcow-1]-pos[atcow])/2.0)*B
                    cost += A + midcost
                    index = endcow
                    #print "WiFi at " + str(pos[atcow]+(pos[endcow-1]-pos[atcow])/2.0) + " which is a midpoint which looks good"

                else:
                    if midcost < prevmidcost+A:
                        midcost = ((pos[endcow]-pos[atcow])/2.0)*B
                        cost += A + midcost
                        index = endcow+1
                        #print "WiFi at " + str(pos[atcow]+(pos[endcow]-pos[atcow])/2.0) + " which is a midpoint which looks good"
                        
                    else:
                        midcost = ((pos[endcow-1]-pos[atcow])/2.0)*B
                        cost += A + midcost
                        index = endcow
                        #print "WiFi at " + str(pos[atcow]+(pos[endcow-1]-pos[atcow])/2.0) + " which is a midpoint which looks good"
                              
    print cost
    x = raw_input()

    
                
            
            




















            
        
    
