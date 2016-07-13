
x = raw_input()

def create(i, n):
    if (n==0):
        return "moo"
    else:
        output = i + "m"+(n+2)*"o"+i
        return output


while( x!= "#"):
    indexR = int(x)
    n=0
    gamestring = "moo"
    
    while (indexR > 2*len(gamestring)+n+4 ):
        n +=1
        gamestring = create(gamestring, n)
        

    
    
    if indexR <= len(gamestring):
        output = gamestring[indexR-1]
    elif indexR == (len(gamestring)+1):
        output = "m"
    elif indexR <= (len(gamestring)+n+4):
        output = "o"
    else:
        indexR = indexR - (len(gamestring)+n+4)
        
        output = gamestring[indexR-1]


    print output
    x = raw_input()


    


