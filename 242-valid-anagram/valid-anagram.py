class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 0
            hm[c] += 1
        
        for c in t:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] -= 1
        
        
        return min(hm.values()) == max(hm.values()) == 0

        