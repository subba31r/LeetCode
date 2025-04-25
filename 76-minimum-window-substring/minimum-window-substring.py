class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        dicT = {}
        for i in t:
            dicT[i] = dicT.get(i,0) + 1
        
        dicS ={}
        tlen = len(dicT)
        ans = [-1,0,0]
        l = 0
        cur = 0
        for r in range(0,len(s)):
            dicS[s[r]] = dicS.get(s[r],0) + 1
            if s[r] in dicT and dicS[s[r]] == dicT[s[r]]:
                cur += 1
            while l<=r and cur==tlen:
                ch = s[l]
                if ans[0] == -1 or ans[0]>=r-l+1:
                    ans[0] = r-l+1
                    ans[1] = l
                    ans[2] = r
                dicS[ch] -= 1
                if ch in dicT and dicS[ch] < dicT[ch]:
                    cur -=1
                l += 1
        if ans[0] == -1:
            return ""
        return s[ans[1]:ans[2]+1]


            