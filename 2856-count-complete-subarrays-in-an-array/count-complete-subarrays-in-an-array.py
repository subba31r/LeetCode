class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = len(set(nums))
        n = len(nums)
        res = 0
        for i in range(0,n):
            temp = set()
            for j in range(i,n):
                temp.add(nums[j])
                if len(temp) == count:
                    res += (n-j)
                    break
        return res