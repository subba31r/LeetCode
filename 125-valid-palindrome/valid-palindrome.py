class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for c in s:
            temp = ord(c)-ord('a')
            if temp>= 0 and temp<=25:
                t = t+c
            if c in "0123456789":
                t = t+c
        return t == t[::-1]