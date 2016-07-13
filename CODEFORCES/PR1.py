b = int(raw_input())
Boys = raw_input().split()
g = int(raw_input())
Girls = raw_input().split()

for i in range(len(Boys)):
    Boys[i] = int(Boys[i])
for i in range(len(Girls)):
    Girls[i] = int(Girls[i])

Boys.sort()
Girls.sort()

pairs = 0

bindex = 0
gindex = 0

while (bindex<len(Boys) and gindex<len(Girls)):
    diff = Boys[bindex]-Girls[gindex]
    if abs(diff) <= 1: #got a pair
        pairs += 1
        bindex += 1
        gindex += 1
    else:
        if diff > 0:
            gindex += 1
        else:
            bindex += 1
print pairs
        


