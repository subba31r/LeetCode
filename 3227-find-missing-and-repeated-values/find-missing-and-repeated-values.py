class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [1]*(n**2)
        for i in range(n):
            for j in range(n):
                res[grid[i][j]-1] -= 1
        a,b = 0, 0
        for i in range(len(res)):
            if res[i] == -1:
                a= i+1
            if res[i] == 1:
                b = i+1
        return [a,b]
