class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if len(str1) == len(str2) and str1 != str2:
            return ""
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        res=""
        prefix = str1[0]
        for i in range(1,len(str1)):
            temp2 = prefix*(len(str2)//len(prefix))
            temp1 = prefix*(len(str1)//len(prefix))
            if temp2 == str2 and temp1 == str1:
                res = prefix
            prefix = prefix+str1[i]
        temp2 = prefix*(len(str2)//len(prefix))
        temp1 = prefix*(len(str1)//len(prefix))
        if temp2 == str2 and temp1 == str1:
            res=prefix
        return res

