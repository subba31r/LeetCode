class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ch = {}
        res = 0
        st = 0
        for i in range(len(s)):
            ch[s[i]] = ch.get(s[i],0)+1
            while len(ch) == 3:
                res = res + len(s) - i
                ch[s[st]] -= 1
                if ch[s[st]] == 0:
                    del ch[s[st]]
                st += 1
        return res
