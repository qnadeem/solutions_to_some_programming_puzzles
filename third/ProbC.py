import copy

def create(y, x):
    p = []
    for i in range(x):
        p = p + [0]
    paint = []
    for i in range(y):
        paint = paint + [list(p)]
    return paint

def dfs(graph, pastures, string, x):
    
    pastures[x] = string # set orig box to 0
    
    if string == "J":
        s = "F"
    elif string == "F":
        s="J"   # getting s for next recursive call 


    for i in range(len(graph[x])):
        
        if graph[x][i] == 1: #path between this pasture and the other
            if pastures[i] == "U":
                #RECURSE
                worked = dfs(graph, pastures, s, i)
                if not worked: return False
            elif pastures[i] == string:
                #good already done
                return False

    return True

def getJs(G, n):
    
     pastures = []
     
     for i in range(n):
         pastures = pastures+["U"] #unmarked
                    

     
            
        

        worked = dfs(G,pastures,"J", q)

        if not worked: return -1
        #else keep looping while unmarked pastures left.

    #outside loop. done.. Count Js.

     Js = 0
     for i in pastures:
         if i=="J":
             Js+=1
     return Js

    
    


x = str(raw_input())
while( x!= "#"):
    NandM = x.split()
    n = int(NandM[0])

    m = int(NandM[1])


    graph = create(n, 0)
    
    for i in range(m):
        pathh = raw_input()
        pathh = pathh.split()
        a = int(pathh[0])
        b = int(pathh[1])
        #a and b are the two pastures, this path connects 
        graph[a-1].append(b-1) # b is stored at index b-1 and same for a.
        graph[b-1].append(a-1)

    #Graph is now an adjaceny matrix with all the pastures's connections.

    ans = getJs(graph, n)

    print ans
        
    x = raw_input()
