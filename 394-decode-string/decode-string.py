class Solution:
    def decodeString(self, s: str) -> str:
        num = "0123456789"
        st = []
        for i in range(0,len(s)):
            if s[i] in num and s[i-1] in num:
                t = st[-1] + s[i]
                st.pop(-1)
                st.append(t)
            elif s[i] != "]":
                st.append(s[i])
            else:
                temp = ""
                while st[-1] != "[":
                    temp = st[-1] + temp
                    st.pop(-1)
                st.pop(-1)
                temp = temp*int(st[-1])
                st.pop(-1)
                st.append(temp)
            print(st)
        # print(st)
        return "".join(st)
