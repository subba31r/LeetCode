class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0: return False
        target = total // 2
        li = set([0])

        for num in nums:
            for cur in list(li):
                temp = cur + num
                if temp == target: return True
                li.add(temp)
        return False
                
