class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in range(0,len(s)):
            if s[i] != "*":
                st.append(s[i])
            elif len(st) != 0 and s[i] == "*":
                st.pop(-1)
        return "".join(st)