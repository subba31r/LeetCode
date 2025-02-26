class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxEle = max(nums)
        dp = [0]*(maxEle+1)
        n = len(nums)
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 0
            hm[n] += 1

        if 1 in hm:
            dp[1] = hm[1]

        for i in range(2,len(dp)):
            dp[i] = max(i*hm.get(i,0) + dp[i-2],dp[i-1])

        return dp[len(dp)-1]