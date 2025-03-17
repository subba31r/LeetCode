class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        zeros = 0
        l = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while l < len(nums) and zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
                cur -= 1
            cur += 1
            res = max(res,cur)
        if zeros == 0:
            zeros = 1
        return res-zeros
