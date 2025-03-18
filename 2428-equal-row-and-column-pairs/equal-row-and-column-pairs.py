class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm = {}
        res = 0
        for i in range(0,len(grid)):
            if str(grid[i]) not in hm:
                hm[str(grid[i])] = 0
            hm[str(grid[i])] += 1

        for i in range(0,len(grid)):
            t = []
            for j in range(0,len(grid)):
                t.append(grid[j][i])
            if str(t) in hm:
                res += hm[str(t)]

        return res