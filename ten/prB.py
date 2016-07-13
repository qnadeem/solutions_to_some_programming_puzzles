def Area(a,b,k):
    xdiff = abs(a[0]-b[0])
    ydiff = abs(a[1]-b[1])

    if(xdiff<k and ydiff<k):#both squares touch.
        #return overlap
        return (k-xdiff)*(k-ydiff)
    else:
        return 0

def overlap(slist,N,k):
    clashes = 0
    area = 0

    for x in range(N):
        for y in range(x+1,N):
            t = Area(slist[x],slist[y],k)
            if t>0:
                area = t
                clashes += 1
            if clashes==2:
                return -1

    if clashes==1:
        return area
    else:
        return 0

#x = raw_input()
fo = open("C.in", "r")
x = fo.readline()

while( x!= "#"):
    x = x.split()
    N = int(x[0])
    K = int(x[1])

    squares = []

    for i in range(N):
        #x = raw_input()
        x = fo.readline()        
        x = x.split()
        squares.append((int(x[0]),int(x[1])))

    squares.sort(key = lambda t: t[0])
    print squares
        
    #print overlap(squares,N,K)       
    x = fo.readline()


















            
        
    
