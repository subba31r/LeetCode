class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        res = float('inf')
        cur = 0
        while r<n:
            cur = cur + nums[r]
            while cur>=target:
                res = min(res, r-l+1)
                cur = cur - nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0
