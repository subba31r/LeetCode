class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        temp = sorted(nums)
        if temp == nums:
            return 0

        for i in range(len(nums)):
            nums = nums[-1:] + nums[:-1]
            if nums == temp:
                return i+1
        return -1