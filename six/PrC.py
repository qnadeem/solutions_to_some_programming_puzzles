import math 


def create(y, x):
    p = []
    for i in range(x):
        p = p + [-1]
    paint = []
    for i in range(y):
        paint = paint + [list(p)]
    return paint


        

    

x = str(raw_input())

while( x!= "#"):
    dimen = x.split()
    N = int(dimen[0]) #height
    K = int(dimen[1])

    if K == 0 :
        print math.pow(3,N)

    else:
        S = []
        D = []
        for i in range(K):
            r = raw_input()
            tri = r.split()
            if tri[0]=="S":
                
        
    
    
    
 
    
    x = raw_input()
