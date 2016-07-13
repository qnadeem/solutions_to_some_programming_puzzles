x = raw_input()

while( x!= "#"):
    x = x.split()
    D = int(x[0])
    H = int(x[1])
    M = int(x[2])

    #bessie began on 11 11: 11.

    if (D==11) and (H<11 or (H==11 and M<11)):
        print -1

    else:
        daydiff = D-11

        # bessie started at 11*60+11 = 671

        end = (H*60)+M

        mindiff = end-671

        totaltime = (daydiff*1440)+mindiff

        print totaltime

    x = raw_input()

    
    




















            
        
    
