x = raw_input()
x = x.split()

B = [int(x[0]), int(x[1]), int(x[2])]

summ = sum(B)
B.sort()
table = 0


while summ>2 and B[2]>0 and B[1]>0:
    possFMax = B[2]/2
    left = B[2]%2

    if B == [1,1,1]:
        table +=1
        B = [0,0,0]

    elif possFMax <= (B[1]+B[0]):
        B[2] = left

        table += possFMax

        if possFMax <= B[1]:
            B[1] -= possFMax
        else:
            B[0] = B[0] - (possFMax-B[1])
            B[1] = 0

    else:
        increase = possFMax - (B[1]+B[0])
        table += increase

        B[1] = 0
        B[0] = 0
        B[2] = B[2] - 2*possFMax

    B.sort()
    summ = sum(B)
    
print table