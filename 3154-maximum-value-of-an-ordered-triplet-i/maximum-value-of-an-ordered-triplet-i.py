class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                t = nums[i]-nums[j]
                if t>0:
                    for k in range(j+1,len(nums)):
                        res = max(res,t*nums[k])
        return res