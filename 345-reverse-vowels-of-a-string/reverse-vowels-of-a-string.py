class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                s = s[:l] + s[r] + s[l+1:r] + s[l] + s[r+1:]
                # s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1
            elif s[r] in vowels:
                 l+=1
            else:
                r -= 1
                l += 1
        return s

        