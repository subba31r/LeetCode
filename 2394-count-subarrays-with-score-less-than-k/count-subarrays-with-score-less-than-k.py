class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res, total = 0, 0
        l = 0
        for r in range(n):
            total += nums[r]
            while r>=l and total*(r-l+1) >= k:
                total -= nums[l]
                l+=1
            res += r-l+1
        return res
