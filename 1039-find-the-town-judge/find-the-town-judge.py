class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for v1, v2 in trust:
            adj[v1-1].append(v2-1)
        
        res = -1
        temp = True
        for i in range(0,len(adj)):
            if len(adj[i]) == 0:
                res =i+1
        
        for i in range(0,len(adj)):
            
            if i != res-1 and res-1 not in adj[i]:
                temp = False

        if temp:
            return res
        return -1