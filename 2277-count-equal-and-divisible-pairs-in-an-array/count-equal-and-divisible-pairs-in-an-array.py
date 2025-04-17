class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # nums[i] == nums[j]
        # i*j % k == 0
        res = 0
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    res += 1
        return res        