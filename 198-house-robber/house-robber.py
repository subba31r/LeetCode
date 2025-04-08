class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]
        maxEle = dp[1]
        for i in range(2,n+1):
            #considering till the previous house the amount we loot
            #and the current house loot
            #if the current house loot till where we reached is less
            #than the previous house we continue with previous house loot
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
            maxEle = max(maxEle,dp[i])
        return maxEle