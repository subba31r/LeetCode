class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n > 0:
            val = n%26
            if val == 0:
                n=n-26
            n=n//26
            if val == 0:
                res = "Z" + res
            else:
                res = chr(val + 64) + res
        return res
            
        