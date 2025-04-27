class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)-2):
            s = nums[i] + nums[i+2]
            if s == nums[i+1]/2:
                res += 1
        return res
