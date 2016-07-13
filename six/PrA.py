x = str(raw_input())

def printt(a):
    r = ""

    if a ==0:
        print "0"

    else:
        while a>0:
            i = a%2
            a = a/2
            r = str(i) + r

    

        print r
        





while( x!= "#"):

    N = int(x, 2)    
    ans = 17*N
    printt(ans)

  
    
    x = raw_input()
