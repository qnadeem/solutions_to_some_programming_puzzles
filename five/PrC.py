from bisect import bisect_left

word_fragment = 'aa'

wordlist = ['aa','aaa','aab','ab','abc', 'bde','rdb','vvv', 'w','z']


ans = wordlist[bisect_left(wordlist, word_fragment):
         bisect_left(wordlist, word_fragment[:-1] + chr(ord(word_fragment[-1])+1))]

print ans
