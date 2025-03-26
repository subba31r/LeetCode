class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums =[]
        for row in grid:
            for num in row:
                nums.append(num)
        
        nums.sort()
        n = len(nums)
        mid = nums[n//2]
        res = 0
        for num in nums:
            if num%x != mid%x:
                return -1
            res += abs(mid-num)//x
        return res
            