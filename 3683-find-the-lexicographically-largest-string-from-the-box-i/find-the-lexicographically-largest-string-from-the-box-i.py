from itertools import combinations
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        
        n = len(word)
        res = ""
        val = n-numFriends+1
        for i in range(0,n):
            res = max(res,word[i:min(i+val,n)])
        return res


