
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = Counter(arr)
        t = set()

        for k in hm:
            if hm[k] in t:
                return False
            t.add(hm[k])
        return True