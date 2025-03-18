class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        pre = 0
        for i in range(len(nums)):
            while pre & nums[i] != 0:
                pre ^= nums[cur]
                cur += 1
            pre |= nums[i]
            res = max(res,i-cur+1)
        return res