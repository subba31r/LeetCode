class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1]*n
        for i in range(1,n):
            forward[i] = forward[i-1]*nums[i-1]

        backward = 1
        for i in range(n-1,-1,-1):
            forward[i] *= backward
            backward *= nums[i]
        return forward
