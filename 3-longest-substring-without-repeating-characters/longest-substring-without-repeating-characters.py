class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set()
        n = len(s)
        l,r = 0,0
        cur = 0
        res = 0
        while r < n:
            if s[r] not in t:
                t.add(s[r])
                r += 1
                cur += 1
            else:
                res = max(cur, res)
                while s[r] in t:
                    t.remove(s[l])
                    cur -= 1
                    l += 1
        res = max(cur,res)
        return res