class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        zeros = 0
        count = 0
        l = 0
        for r in range(0,len(nums)):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                count -= 1
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            count += 1
            res = max(res,count)
        return res
            