class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return 0
        ans = strs[0]
        for s in strs[1:]:
            while not s.startswith(ans):
                #if the string doesn't start with the given prefix we decrease the prefix and check again
                ans = ans[:-1]
                if not ans:
                    return ""
        return ans