class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2 + (n-1)**2
        # n = 1 -> 1 -> 1 
        # n = 2 -> 5 -> 1 + 3 + 1
        # n = 3 -> 13 -> 1 + 3 + 5 + 3 + 1
        # n = 4 -> 25 -> 1 + 3 + 5 + 7 + 5 + 3 + 1
