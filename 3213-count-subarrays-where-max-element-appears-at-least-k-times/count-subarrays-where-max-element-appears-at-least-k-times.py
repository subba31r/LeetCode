class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)
        res, count, l = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == maxEle:
                count += 1
            while count == k:
                if nums[l] == maxEle:
                    count -= 1
                l+=1
            res += l
        return res