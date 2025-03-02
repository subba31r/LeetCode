class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        
        idx = -1
        for i in range(n):
            if nums[i] == 0 and idx == -1:
                idx = i
            elif idx != -1 and nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx = idx+1 
        return nums
        
