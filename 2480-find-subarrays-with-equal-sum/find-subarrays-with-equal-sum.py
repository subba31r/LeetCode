class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hm = {}
        pre = nums[0]
        for i in range(1,len(nums)):
            cur = pre + nums[i]
            if cur in hm:
                return True
            hm[cur] = 1
            pre = nums[i]
        return False
