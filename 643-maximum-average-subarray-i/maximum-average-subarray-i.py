class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float('-inf')
        cur = 0
        l=0
        for r in range(0,len(nums)):
            cur += nums[r]
            if r>= k-1:
                temp = cur/k
                res = max(temp,res)
                cur = cur-nums[l]
                l += 1
        return res