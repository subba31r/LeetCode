class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        hm1 = Counter(word1)
        hm2 = Counter(word2)
        val1 = list(hm1.values())
        val1.sort()
        val2 = list(hm2.values())
        val2.sort()
        if val1 == val2:
            return True
        return False

        # abbzzca -> a-2, b-2, c-1, z-2
        # babzzcz -> a-1, b-2, z-3, c-1