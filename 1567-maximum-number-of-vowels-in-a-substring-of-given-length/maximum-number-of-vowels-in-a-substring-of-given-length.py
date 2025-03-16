class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        res = 0
        l=0
        cur = 0
        for r in range(0,len(s)):
            if s[r] in vowels:
                cur += 1
            if r>= k-1:
                res = max(res,cur)
                if s[l] in vowels:
                    cur -= 1
                l += 1
        return res
