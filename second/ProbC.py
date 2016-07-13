def gettwos(x):
    result = []

    for i in range(len(x)):
        bit = x[i]
        if bit == "0":
            temp = x[0:i]+"1"
            if i<(len(x)-1): temp += x[i+1:]
        else:
            temp = x[0:i]+"0"
            if i<(len(x)-1): temp += x[i+1:]

        result.append(temp)
    return result

def getthrees(x):
    result = []

    for i in range(len(x)):
        bit = x[i]
        if bit == "0":
            temp = x[0:i]+"1"
            if i<(len(x)-1): temp += x[i+1:]
            result.append(temp)
            
            temp2 = x[0:i]+"2"
            if i<(len(x)-1): temp2 += x[i+1:]
            result.append(temp2)
            

        elif bit == "1":
            temp = x[0:i]+"0"
            if i<(len(x)-1): temp += x[i+1:]
            result.append(temp)

            temp2 = x[0:i]+"2"
            if i<(len(x)-1): temp2 += x[i+1:]
            result.append(temp2)

        else:
            temp = x[0:i]+"0"
            if i<(len(x)-1): temp += x[i+1:]
            result.append(temp)

            temp2 = x[0:i]+"1"
            if i<(len(x)-1): temp2 += x[i+1:]
            result.append(temp2)
        
    return result          
            
def converttoD(x):
    for p in range(len(x)):
        string = x[p]
        numb = int(string, 2)
        x[p] = numb

def converttoDfromT(x):
    for p in range(len(x)):
        string = x[p]
        numb = int(string, 3)
        x[p] = numb

def getsame(A, B):
    ans = 0
    for x in A:
        if x in B: ans = x
    return ans

x = raw_input()

while( x!= "#"):
    
    bTwo = x
    bthree = raw_input()

    allTWO = gettwos(bTwo) 
    allTHREE = getthrees(bthree)

    converttoD(allTWO)
    converttoDfromT(allTHREE)

    ANS = getsame(allTWO, allTHREE)
    print ANS


    x = raw_input()

