class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ele = max(candies)
        res = []
        for c in candies:
            if c+extraCandies >= ele:
                res.append(True)
            else:
                res.append(False)
        return res