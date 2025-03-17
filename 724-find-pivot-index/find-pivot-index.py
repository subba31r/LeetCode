class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)
        res = -1
        for i in range(0,len(nums)):
            rightsum = rightsum - nums[i]
            if leftsum == rightsum:
                res = i
                break
            leftsum = leftsum + nums[i]
        return res