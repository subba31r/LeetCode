class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        n, m = len(grid), len(grid[0])
        dr = 0
        pick = True
        for i in range(n):
            for j in range(m):
                if pick:
                    pick = False
                    if dr == 1:
                        res.append(grid[i][m-1-j])
                    else:
                        res.append(grid[i][j])
                else:
                    pick = True
            dr ^= 1
        return res
