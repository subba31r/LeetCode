class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pw = [weights[i]+weights[i+1] for i in range(n-1)]
        pw.sort()
        ans = 0
        for i in range(k-1):
            ans += pw[n-2-i] - pw[i]
        return ans
