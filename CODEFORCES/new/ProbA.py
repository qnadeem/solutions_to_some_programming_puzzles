
x = raw_input()
x = x.split()

s = 0
for i in x:
    s += int(i)

if s == 0:
    print -1
elif s%5==0:
    print s/5
else:
    print -1





