class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res, prefix = 0, 0
        cnt = Counter([0])
        for i in range(0,len(nums)):
            prefix += 1 if nums[i]%modulo == k else 0
            res += cnt[(prefix-k+modulo)%modulo]
            cnt[prefix%modulo] += 1
        return res