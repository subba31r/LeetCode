class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def countKConsonants(k):
            vowels = "aeiou"
            vowel_map = {}
            consonants = 0
            l = 0
            ans = 0
            for r in range(len(word)):
                if word[r] in vowels:
                    vowel_map[word[r]] = vowel_map.get(word[r],0)+1
                else:
                    consonants += 1

                while len(vowel_map) == 5 and consonants >= k:
                    ans += len(word)-r
                    if word[l] in vowels:
                        vowel_map[word[l]] -= 1
                        if vowel_map[word[l]] == 0:
                            del vowel_map[word[l]]
                    else:
                        consonants -= 1
                    l += 1
            return ans
        return countKConsonants(k)-countKConsonants(k+1)