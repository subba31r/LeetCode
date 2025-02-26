class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for n in nums:
            cur = cur+n
            if cur == 0:
                res += 1
        return res