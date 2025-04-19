class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lb(nums,upper+1) - self.lb(nums,lower)
    def lb(self,nums,value):
        l,r = 0, len(nums)-1
        res = 0
        while l < r:
            s = nums[l] + nums[r]
            if s < value:
                res += r-l
                l += 1
            else:
                r -= 1
        return res
