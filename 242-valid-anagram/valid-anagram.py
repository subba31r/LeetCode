class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #If both strings are not of same length
        # if len(s) != len(t):
        #     return False
        # dic = {}
        # for i in range(0,len(s)):
        #     if s[i] in dic:
        #         dic[s[i]] += 1
        #     else:
        #         dic[s[i]] = 1
            
        #     if t[i] in dic:
        #         dic[t[i]] -= 1
        #     else:
        #         dic[t[i]] = -1
        
        # for k in dic:
        #     if dic[k] != 0:
        #         return False
        
        # return True

        if len(s) != len(t):
            return False
        
        sSet = set(s)
        for i in sSet:
            if s.count(i) != t.count(i):
                return False
        return True


        