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


As a human being, you have no choice about the fact that you need a philosophy. Your only choice is whether you define your philosophy by a conscious, rational, disciplined process of thought and scrupulously logical deliberation — or let your subconscious accumulate a junk heap of unwarranted conclusions, false generalizations, undefined contradictions, undigested slogans, unidentified wishes, doubts and fears, thrown together by chance, but integrated by your subconscious into a kind of mongrel philosophy and fused into a single, solid weight: self-doubt, like a ball and chain in the place where your mind's wings should have grown.

 Nice! haha I'm going to read Kant and Aristotle's ethical theories next in class  I remember my philosophy proff making fun of Ayn Rand bcs she's an egoist. this article's very interesting though
