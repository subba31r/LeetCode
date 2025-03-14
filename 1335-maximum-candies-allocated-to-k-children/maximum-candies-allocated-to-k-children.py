class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)
        res = 0

        while l <= r:
            m = (l+r)//2
            count = sum(c//m for c in candies)
            if count >= k:
                res = m
                l = m+1
            else:
                r = m-1
        return res

