class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Arr = [0]*26
        s2Arr = [0]*26
        for i in range(0,len(s1)):
            t1 = ord(s1[i]) - ord('a')
            t2 = ord(s2[i]) - ord('a')
            s1Arr[t1] += 1
            s2Arr[t2] += 1
        
        
        l = 0
        for r in range(len(s1),len(s2)):
            if s1Arr == s2Arr:
                return True
            t2 = ord(s2[l]) - ord('a')
            s2Arr[t2] -= 1
            l += 1
            t1 = ord(s2[r]) - ord('a')
            s2Arr[t1] += 1
        if s1Arr == s2Arr:
            return True
        return False
        
