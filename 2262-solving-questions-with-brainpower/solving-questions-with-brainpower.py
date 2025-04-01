class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        dp[-1] = questions[-1][0]
        for i in range(n-2,-1,-1):
            p, b = questions[i]
            if i+b+1 < n: p +=dp[i+b+1]
            dp[i] = max(p,dp[i+1])
        return dp[0]