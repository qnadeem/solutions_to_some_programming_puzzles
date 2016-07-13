def create(y, x):
    p = []
    for i in range(x):
        p = p + [-1]
    paint = []
    for i in range(y):
        paint = paint + [list(p)]
    return paint

def getshortest(X, Y, grid, H, W, visited, maxElevDiff):
    #x1 and x2 are two WPs. x1 --> x2
    y1,x1 = X[0], X[1]
    
    if X==Y: #both WPs equal
        return maxElevDiff

    else:
        visited[y1][x1] = 0 #visited this
        differences = []

        if x1 + 1 < W and visited[y1][x1+1]!=0:
            elevation = abs(grid[y1][x1]-grid[y1][x1+1])
            #dist from x1+1 to x2.. and add it to elevation
            if elevation > maxElevDiff:
                R1 = getshortest((y1,x1+1),Y,grid,H,W,visited, elevation)

            else:
                R1 = getshortest((y1,x1+1),Y,grid,H,W,visited, maxElevDiff)
            minimumdist.append(R1)

        if x1 - 1 >= 0 and visited[y1][x1-1]!=0:
            elevation = abs(grid[y1][x1]-grid[y1][x1-1])
            #dist from x1+1 to x2.. and add it to elevation
            if elevation > maxElevDiff:
                R2 = getshortest((y1,x1-1),Y,grid,H,W,visited, elevation)
            else:
                R2 = getshortest((y1,x1-1),Y,grid,H,W,visited, maxElevDiff)
            minimumdist.append(R2)

        if y1 + 1 < H and visited[y1+1][x1]!=0:
            elevation = abs(grid[y1+1][x1]-grid[y1][x1])
            #dist from x1+1 to x2.. and add it to elevation
            if elevation 
                R = elevation+getshortest((y1+1,x1),Y,grid,H,W,visited)
            minimumdist.append(R)

        if y1 - 1 >= 0 and visited[y1-1][x1]!=0:
            elevation = abs(grid[y1-1][x1]-grid[y1][x1])
            #dist from x1+1 to x2.. and add it to elevation
            R = elevation+getshortest((y1-1,x1),Y,grid,H,W,visited)
            minimumdist.append(R)

        if minimumdist== []: return 0
        return min(minimumdist)

        
        

    

def difficulty(WP ,grid, H, W):
    difficulty = 0

    for i in range(len(WP)-1): #go to all but the last WP
        pathsfromthisWP = []
        visited = create(H,W)

        for x in range(i+1,len(WP)): #go from i+1 WP to last WP
            dist = getshortest(WP[i],WP[x], grid, H, W, visited, 0)
            #^get shortest path distance between the two WPs.
            pathsfromthisWP.append(dist)
        r = max(pathsfromthisWP)
        if r > difficulty:
            difficulty = r

    return difficulty
    

x = str(raw_input())

while( x!= "#"):
    dimen = x.split()
    H = int(dimen[0]) #height
    W = int(dimen[1])

    grid = create(H, W)
    
    for i in range(H):
        row = raw_input()
        row = row.split()
        for p in range(W):
            grid[i][p] = int(row[p])
    # Got the grid! ^
    waypoints = []
    for i in range(H):
        row = raw_input()
        row = row.split()
        for p in range(W):
            if row[p] == "1":
                waypoints.append((i,p))
    #we have waypoints too. now check smalles distance such that
    # all waypoints can get to each other.

    ans = difficulty(waypoints, grid, H, W)
    
    print ans
    
    x = raw_input()
