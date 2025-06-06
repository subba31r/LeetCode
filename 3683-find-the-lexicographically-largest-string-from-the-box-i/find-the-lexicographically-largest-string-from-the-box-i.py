from itertools import combinations
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # word -> dbca 
        # no.of friends -> 2

        # d bca
        # db ca
        # dbc a
        # 4 - 2 + 1 = 3
        if numFriends==1:
            return word
        n = len(word)
        
        res = []
        val = n-numFriends+1
        for i in range(0,n-val+1):
            s = word[i:i+val]
            res.append(s)
        
        for i in range(n-val+1,n):
            s = word[i:]
            res.append(s)
        res.sort()
        return res[-1]


