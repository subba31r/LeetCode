class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        l=0
        for r in range(0,len(t)):
            if l<len(s) and t[r] == s[l]:
                l += 1
        return True if l>=len(s) else False
        
        
        

