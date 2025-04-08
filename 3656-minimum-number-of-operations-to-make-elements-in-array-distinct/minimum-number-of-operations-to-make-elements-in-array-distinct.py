class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hm = {}
        for i in range(0,len(nums)):
            if nums[i] not in hm:
                hm[nums[i]] = 0
            hm[nums[i]] += 1
        
        
        res = 0
        for i in range(0,len(nums),3):
            if len(hm) == len(nums)-i:
                return res
            j = 0
            while j < 3 and j+i < len(nums):
                hm[nums[i+j]] = hm[nums[i+j]] - 1
                if hm[nums[i+j]] == 0:
                    del hm[nums[i+j]]
                j += 1
            res += 1
            
        return res