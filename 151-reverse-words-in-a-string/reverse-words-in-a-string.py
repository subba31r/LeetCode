class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # st = []
        # temp = ""
        # for i in range(0,len(s)):
        #     if s[i] == " " and temp != "":
        #         st.append(temp)
        #         temp = ""
        #     elif s[i] != " ":
        #         temp = temp + s[i]
        # if temp != "":
        #     st.append(temp)
        # print(st)
        # return " ".join(st[::-1])
        return " ".join(s.split()[::-1])
