class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
        res = 0 
        for num in hm.keys():
            cur = 1
            if num-1 not in hm:
                while num+1 in hm:
                    num = num +1
                    cur += 1
            res = max(res,cur)
        return res
