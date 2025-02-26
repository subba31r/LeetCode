class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        hm = {}
        res = 0
        for i in range(len(s)):
            hm[s[i]] = i
        
        for i in range(len(t)):
            res = res + abs(i-hm[t[i]])
        return res