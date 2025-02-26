class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #brute force 
        # res = 0
        # for i in range(0,len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

        #optimal by using prefix sum - keeping track of already found sums
        prefix_sum = {0:1}
        cur = 0
        res = 0
        for num in nums:
            cur = cur + num
            if (cur-k) in prefix_sum:
                res = res + prefix_sum[cur-k]
            if cur in prefix_sum:
                prefix_sum[cur] += 1
            else:
                prefix_sum[cur] = 1
        return res                                