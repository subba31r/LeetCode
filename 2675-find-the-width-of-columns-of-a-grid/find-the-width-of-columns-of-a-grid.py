class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        arr = [0]*n
        for i in range(0,m):
            for j in range(0,n):
                s = str(grid[i][j])
                arr[j] = max(arr[j],len(s))
        return arr
