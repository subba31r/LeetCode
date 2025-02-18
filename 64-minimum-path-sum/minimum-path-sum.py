class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        res = [[float('inf')]*(cols+1) for _ in range(rows+1)]      
        res[rows][cols-1] = 0
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                val = min(grid[r][c]+res[r+1][c], grid[r][c]+res[r][c+1])
                res[r][c] = val
        return res[0][0]