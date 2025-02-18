class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, 0
        p_len = len(p)
        arrP = [0]*26
        for ch in p:
            val = ord(ch)-ord('a')
            arrP[val] += 1
        s_len = len(s)
        res = []
        arrS = [0]*26
        while r<s_len:
            val = ord(s[r]) - ord('a')
            arrS[val] += 1
            while (r-l+1) > p_len:
                val = ord(s[l]) - ord('a')
                arrS[val] -= 1
                l += 1
            if arrS == arrP:
                res.append(l)
            r += 1
        return res