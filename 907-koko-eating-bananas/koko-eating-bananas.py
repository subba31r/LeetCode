class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        while l<=r:
            m = (l+r)//2
            cur = 0
            for pile in piles:
                cur += pile//m
                pile = pile%m
                if pile%m !=0:
                    cur += 1
            if cur <= h:
                r = m-1
            else:
                l = m+1
        return l
