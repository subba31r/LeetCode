class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0,len(nums)):
            val = target-nums[i]
            if val not in dic:
                dic[nums[i]] = i
            else:
                return [dic[val], i]