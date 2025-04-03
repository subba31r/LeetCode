class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = [0]*n
        right = [0]*n
        for i in range(1,n):
            left[i] = max(left[i-1],nums[i-1])
            right[n-i-1] = max(right[n-i],nums[n-i])
        
        res = 0
        for j in range(1,n-1):
            res = max(res, (left[j]-nums[j])*right[j])
        return res