class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(0,len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         t = nums[i]-nums[j]
        #         if t>0:
        #             for k in range(j+1,len(nums)):
        #                 res = max(res,t*nums[k])
        # return res
        
        #by calculating prefix sum arrays from left and right
        n = len(nums)
        left = [0]*n
        right = [0]*n

        for i in range(1,n):
            left[i] = max(left[i-1],nums[i-1])
            right[n-i-1] = max(right[n-i],nums[n-i])
        
        res = 0
        for j in range(1,n-1):
            res = max(res,(left[j]-nums[j])*right[j])
        return res