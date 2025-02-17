class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        #forward pass
        pre = 1
        for i in range(0,len(nums)):
            res[i] = pre
            pre = pre*nums[i]
        #backward pass
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*post
            post = nums[i]*post
        return res
                
        