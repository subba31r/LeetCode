class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hm = {}
        for s, d in paths:
            hm[s] = d
        start = paths[0][0]
        while start in hm:
            start = hm[start]
        return start