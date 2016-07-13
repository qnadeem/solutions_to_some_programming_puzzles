from bisect import bisect_left

def dotask(AW, dictt, t):
     #t -> challenge
    prefix = t[1]
    Ki = t[0]

    RelevantWords = AW[bisect_left(AW, prefix):
         bisect_left(AW, prefix[:-1] + chr(ord(prefix[-1])+1))]
    # get all words that start with 'prefix'
    # Uses binary search twice to find the right end point (first relevant word)
    # and left end point (last relevant) in the sorted list AW

    if len(RelevantWords) < Ki:
        return -1
    else:
        word = RelevantWords[Ki-1]
        return dictt[word] #return original position of word.

x = raw_input()

while(x!= "#"):
    x = x.split()

    W = int(x[0])
    N = int(x[1])

    allWords = []
    dictt = {}  # stores original index of all words.

    for i in range(W):
        x1 = raw_input()
        dictt[x1] = i+1
        allWords.append(x1)
        #adding all W,i to dictt
        
    allWords.sort() #all words sorted.

    #get challenges now.
    challenges = [] #tuple of challenges.
    for y in range(N):
        x1 = raw_input()
        x1 = x1.split()
        challenges.append((int(x1[0]),x1[1])) #(integer,word)
    #QUICK SO FAR

    for y in range(N):
        t = challenges[y]
        
        ans = dotask(allWords,dictt,t) #return index of word or -1
        print ans

    x = raw_input()

