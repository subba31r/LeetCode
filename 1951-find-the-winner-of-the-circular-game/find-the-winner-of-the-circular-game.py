class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = [num for num in range(1,n+1)]
        cur = 0
        while len(q) > 1:
            cur = (cur + k-1)%len(q)
            q.pop(cur)
        return q[0]