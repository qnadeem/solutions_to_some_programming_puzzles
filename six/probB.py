import sys
 
sys.setrecursionlimit (100000)

def goback(a): #number of ways to get a from a smaller string
    l = len(a)

    if (l<3) or (l%2==0): #if less than 3 or even, no way!
        return 0

    else:
        ans = 0

        mid = l/2  #second half of string past the half
        
        if a[:mid] == a[mid+1:]:
            ans += 2 + goback(a[mid:])+goback(a[:mid+1])

        if a[:mid] == a[mid:-1]:
            ans += 1 + goback(a[mid:])

        #if a[:mid] == a[mid+1:]: joined with case 1!!
         #   ans += 1 + goback(a[:mid+1])

        if a[1:mid+1] == a[mid+1:]:
            ans += 1 + goback(a[:mid+1])

        return ans


x = str(raw_input())


while( x!= "#"):

    print goback(x)

    
    x = raw_input()
