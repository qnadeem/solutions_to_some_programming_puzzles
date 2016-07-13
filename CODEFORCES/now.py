def maxD(L, l):
    diff = []
    diff.append((L[0]-0)*2)
    for i in range(1,len(L)):
        diff.append(L[i]-L[i-1])
    diff.append((l - L[-1])*2)

    return max(diff)/float(2)

x = raw_input()
x = x.split()
n = int(x[0])
l = int(x[1])

All = raw_input().split()
lanterns = [int(x) for x in All]
lanterns.sort()

print maxD(lanterns, l)
