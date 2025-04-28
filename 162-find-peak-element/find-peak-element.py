class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        while l<=r:
            m = (l+r)//2
            t1 = float('-inf') if m-1 < 0 else nums[m-1]
            t2 = float('-inf') if m+1 >= n else nums[m+1]

            if nums[m] > t1 and nums[m] > t2:
                return m
            elif nums[m] > t1:
                l = m+1
            else:
                r = m-1
         