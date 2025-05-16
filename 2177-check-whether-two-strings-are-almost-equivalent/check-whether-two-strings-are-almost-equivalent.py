class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1 = [0]*26
        w2 = [0]*26
        for w in word1:
            w1[ord(w)-ord('a')]+=1
        for w in word2:
            w2[ord(w)-ord('a')]+=1
        
        for i in range(0,26):
            if abs(w1[i]-w2[i])>3:
                return False
        return True