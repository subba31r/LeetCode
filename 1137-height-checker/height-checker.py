class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        temp = heights.copy()
        temp.sort()
        n = len(heights)
        for i in range(n):
            if heights[i] != temp[i]:
                res += 1
        return res
