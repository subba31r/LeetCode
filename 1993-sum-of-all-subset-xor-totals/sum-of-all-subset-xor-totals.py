class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0
        n = len(nums)
        def subsets(i,li,cur):
            if i==n:
                self.res = self.res + cur
                return
            
            li.append(nums[i])
            subsets(i+1,li,cur^nums[i])

            li.pop(-1)
            subsets(i+1,li,cur)
        subsets(0,[],0)
        return self.res