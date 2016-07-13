import copy

def shortestpath(Y, X):
    closest = [] #change to the 2 points
    check = False

    for q in range(len(X)):
        for w in range(len(Y)):
            x = X[q]
            y = Y[w]
            if check == False:
                R = int(abs(x[0]-y[0])+abs(x[1]-y[1]))-1#pathdist
                closest = [x, y, R]
                check = True

            D = int(abs(x[0]-y[0])+abs(x[1]-y[1]))-1
            if D < closest[2]:
                closest[2] = D
                closest[0] = x
                closest[1] = y
    
    return closest[2]

def create(y, x):
    p = []
    for i in range(x):
        p = p + [-1]
    paint = []
    for i in range(y):
        paint = paint + [list(p)]
    return paint

def dfs(P, y, x, H, W, Ys):
    P[y][x] = "Y" # set orig box to 0
    Ys.append((y,x))

    if (x+1 < W) and P[y][x+1] == "X":
        dfs(P, y, x+1, H, W, Ys)

    if (x-1 >= 0) and P[y][x-1] == "X":
        dfs(P, y, x-1, H, W, Ys)

    if (y+1 < H) and P[y+1][x] == "X":
        dfs(P, y+1, x, H, W, Ys)
        

    if (y-1 >= 0) and P[y-1][x] == "X":
        dfs(P, y-1, x, H, W, Ys)

def findXs(grid, H, W):
    Xs= []
    for q in range(H):
        for w in range(W):
            if grid[q][w]== "X":
                Xs.append((q,w))
    return Xs

x = str(raw_input())

while( x!= "#"):
    dimen = x.split()
    H = int(dimen[0])
    W = int(dimen[1])


    grid = create(H, W)
    gotit = False
    
    for i in range(H):
        row = raw_input()
        for p in range(W):
            grid[i][p] = row[p]
            if gotit==False and row[p] == "X":
                Xmark = [i, p]
                gotit = True
    # Got the grid! ^
    #Xmark is just an "X".
    if H==1 and W==1:
        print 0
    else:
        Ys = []
        dfs(grid, Xmark[0], Xmark[1], H, W, Ys)
        # go thru grid. make one region Y. Add all Ys
        
        Xs = findXs(grid, H, W)
        #add all Xs.

        ans = shortestpath(Ys, Xs)

        print ans
        
    x = raw_input()
