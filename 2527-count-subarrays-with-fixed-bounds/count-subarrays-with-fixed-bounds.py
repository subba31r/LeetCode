class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        maxi, mini = -1, -1
        l = 0
        for r in range(0,len(nums)):
            if nums[r] < minK or nums[r]>maxK:
                l = r+1
                continue
            if nums[r] == maxK: maxi = r
            if nums[r] == minK: mini = r
            res += max((min(maxi,mini)-l+1),0)
        return res
