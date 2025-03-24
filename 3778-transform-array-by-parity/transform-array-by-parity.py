class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even = 0
        for n in nums:
            if n%2 == 0:
                even += 1
        
        for i in range(0,len(nums)):
            if even > 0:
                nums[i] = 0
                even -= 1
            else:
                nums[i] = 1
        return nums