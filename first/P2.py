def create(n):
    p = []
    for i in range(n):
        p = p + [-1]
    paint = []
    for i in range(n):
        paint = paint + [list(p)]
    return paint

def dfs(P, x, y, size):
    letter = P[x][y]

    P[x][y] = 0 # set orig box to 0

    if (x+1 < size) and P[x+1][y] == letter:
        dfs(P, x+1, y, size)

    if (x-1 >= 0) and P[x-1][y] == letter:
        dfs(P, x-1, y, size)

    if (y+1 < size) and P[x][y+1] == letter:
        dfs(P, x, y+1, size)

    if (y-1 >= 0) and P[x][y-1] == letter:
        dfs(P, x, y-1, size)


def getR(P, s):
    regions = 0

    for x in range(size):
        for y in range(size):
            if P[x][y] != 0:
                dfs(P , x, y, size)
                regions += 1

    return regions
    
def getcowP(P, s):
    for x in range(s):
        for y in range(s):
            if P[x][y] == "R":
                P[x][y] = "G"


x = raw_input()

while( x!= "#"):
    size = int(x)

    realP = create(size)
    cP = create(size)
    
    for i in range(size):
        row = raw_input()
        for p in range(size):
            realP[i][p] = row[p]
            cP[i][p] = row[p]

    hregions = getR(realP,size)
    
    getcowP(cP, size)
    cregions = getR(cP, size)
    
    print hregions, cregions    

    x = raw_input()
