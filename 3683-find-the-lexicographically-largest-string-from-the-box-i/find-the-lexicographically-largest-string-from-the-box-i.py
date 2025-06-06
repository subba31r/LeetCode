from itertools import combinations
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        
        n = len(word)
        res = ""
        val = n-numFriends+1
        for i in range(0,n-val+1):
            res = max(res,word[i:i+val])

        for i in range(n-val+1,n):
            res = max(res,word[i:])
        return res


