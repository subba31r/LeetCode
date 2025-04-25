class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}":"{",")":"(","]":"["}
        for ch in s:
            if ch in "{([":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                par = dic[ch]
                if stack[-1] == par:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False