class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = [0]*26
        l = 0
        res = 0
        for r in range(0,len(s)):
            t = ord(s[r]) - ord('A')
            arr[t] += 1
            maxEle = max(arr)
            val = r-l+1-maxEle
            if val <= k:
                res = max(r-l+1,res)
            else:
                te = ord(s[l]) - ord('A')
                arr[te] -= 1
                l += 1
        return res        

