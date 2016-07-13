#where the feet are
FL = [0,1]
FR = [1,1]
RL = [0,0]
RR = [1,0]

#The boundaries where the feet have been!
left = 0
right = 1
up = 1
down = 0

direc = "N"  #current direction


def resetvals():
    global left
    global right
    global up
    global down
    global FL
    global FR
    global RL
    global RR
    global direc
    FL = [0,1]
    FR = [1,1]
    RL = [0,0]
    RR = [1,0]
    left = 0
    right = 1
    up = 1
    down = 0
    direc = "N"

def pivot(move):
    global left
    global right
    global up
    global down
    global FL
    global FR
    global RL
    global RR
    global direc

    if move[0:2] == "FL":

        #rotate FR
        Rx = FL[0]
        Ry = FL[1]
        Px = FR[0] #point to be rotated
        Py = FR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry-FR[0]
        FR[0] = Px
        FR[1] = Py

        #rotate RL
        Rx = FL[0]
        Ry = FL[1]
        Px = RL[0] #point to be rotated
        Py = RL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry-RL[0]
        RL[0] = Px
        RL[1] = Py

        #rotate RR
        Rx = FL[0]
        Ry = FL[1]
        Px = RR[0] #point to be rotated
        Py = RR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry-RR[0]
        RR[0] = Px
        RR[1] = Py
        

    elif move[0:2] == "FR":

        #rotate FL
        Rx = FR[0]
        Ry = FR[1]
        Px = FL[0] #point to be rotated
        Py = FL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- FL[0]
        FL[0] = Px
        FL[1] = Py

        #rotate RL
        
        Px = RL[0] #point to be rotated
        Py = RL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- RL[0]
        RL[0] = Px
        RL[1] = Py

        #rotate RR
       
        Px = RR[0] #point to be rotated
        Py = RR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- RR[0]
        RR[0] = Px
        RR[1] = Py
        


    elif move[0:2] == "RL":
        #rotate FL
        Rx = RL[0]
        Ry = RL[1]
        Px = FL[0] #point to be rotated
        Py = FL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- FL[0]
        FL[0] = Px
        FL[1] = Py

        #rotate FR
        Rx = RL[0]
        Ry = RL[1]
        Px = FR[0] #point to be rotated
        Py = FR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- FR[0]
        FR[0] = Px
        FR[1] = Py

        #rotate RR
        Rx = RL[0]
        Ry = RL[1]
        Px = RR[0] #point to be rotated
        Py = RR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- RR[0]
        RR[0] = Px
        RR[1] = Py



    elif move[0:2] == "RR":
        #rotate FL
        Rx = RR[0]
        Ry = RR[1]
        Px = FL[0] #point to be rotated
        Py = FL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- FL[0]
        FL[0] = Px
        FL[1] = Py

        #rotate FR
        Rx = RR[0]
        Ry = RR[1]
        Px = FR[0] #point to be rotated
        Py = FR[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- FR[0]
        FR[0] = Px
        FR[1] = Py

        #rotate RL
        Rx = RR[0]
        Ry = RR[1]
        Px = RL[0] #point to be rotated
        Py = RL[1] #^

        Px = Rx-Ry+Py   #formula to rotate 90 degree clockwise around a point.
        Py = Rx +Ry- RL[0]
        RL[0] = Px
        RL[1] = Py


    if direc == "N":
        direc = "E"
    elif direc == "E":
        direc = "S"
    elif direc == "S":
        direc = "W"
    elif direc == "W":
        direc = "N"

def movefoot(move):
    global left
    global right
    global up
    global down
    global FL
    global FR
    global RL
    global RR
    global direc

    #which direction to move!
    moveD = move[2] # orig given direction
    #if direc == "N": #keep moveD as is.   
    if direc == "E":
        if moveD == "F": moveD = "R"
        elif moveD == "R" : moveD = "B"
        elif moveD == "B": moveD = "L"
        elif moveD == "L": moveD = "F"

    elif direc == "S":
        if moveD == "F": moveD = "B"
        elif moveD == "R" : moveD = "L"
        elif moveD == "B": moveD = "F"
        elif moveD == "L": moveD = "R"

    elif direc == "W":
        if moveD == "F": moveD = "L"
        elif moveD == "R" : moveD = "F"
        elif moveD == "B": moveD = "R"
        elif moveD == "L": moveD = "B"

    ##move the given foot now

    if move[0:2] == "FR":
        #move FR.
        if moveD == "F":
            FR[1] = FR[1]+1
        elif moveD == "B":
            FR[1] = FR[1]-1
        elif moveD == "R":
            FR[0] = FR[0]+1
        elif moveD == "L":
            FR[0] = FR[0]-1


    elif move[0:2] == "FL":
        #move FL.
        if moveD == "F":
            FL[1] = FL[1]+1
        elif moveD == "B":
            FL[1] = FL[1]-1
        elif moveD == "R":
            FL[0] = FL[0]+1
        elif moveD == "L":
            FL[0] = FL[0]-1

    elif move[0:2] == "RL":
        #move RL.
        if moveD == "F":
            RL[1] = RL[1]+1
        elif moveD == "B":
            RL[1] = RL[1]-1
        elif moveD == "R":
            RL[0] = RL[0]+1
        elif moveD == "L":
            RL[0] = RL[0]-1

    elif move[0:2] == "RR":
        #move RR.
        if moveD == "F":
            RR[1] = RR[1]+1
        elif moveD == "B":
            RR[1] = RR[1]-1
        elif moveD == "R":
            RR[0] = RR[0]+1
        elif moveD == "L":
            RR[0] = RR[0]-1

    if (FL==FR or FL ==RL or FL==RR or FR==RL or FR==RR or RR ==RL):
        return False
    else:
        return True


def changeboundaries():
    global left
    global right
    global up
    global down
    global FL
    global FR
    global RL
    global RR

    X = [ FL[0], FR[0], RL[0], RR[0] ]
    Y = [ FL[1], FR[1], RL[1], RR[1] ]

    if up < max(Y):
        up = max(Y)
    if down > min(Y):
        down = min(Y)
    if left > min(X):
        left = min (X)
    if right < max(X):
        right = max(X)   


def sizeofrectangle():
    global left
    global right
    global up
    global down

    X = abs(right - left) + 1
    Y = abs(up - down) + 1
    return X*Y
    

def dochallenge(moves):
    global left
    global right
    global up
    global down
    global FL
    global FR
    global RL
    global RR
    
    for i in range(moves): # take each move one by one and process the cows' feet etc.
        nextmove = raw_input()
        if (nextmove[2] == "P"):
            pivot(nextmove)  # WRITE THIS
            changeboundaries()
        else:
            legal = movefoot(nextmove)  # WRITE THIS
            if (legal==False):
                return -1
            changeboundaries()

    output = sizeofrectangle()   # WRITE THIS
    return output


x = raw_input()

while( x!= "#"):
    moves = int(x) #how many moves in the following dance challenge.

    output = dochallenge(moves)
    print int(output)

    resetvals()

    x = raw_input()

