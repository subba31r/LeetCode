class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 1, max(nums)

        while l<r:
            m = (l+r)//2
            count = 0
            i = 0
            while i < n:
                if nums[i] <= m:
                    count += 1
                    i += 2
                else:
                    i += 1
            if count >= k:
                r = m
            else:
                l = m+1
        return l