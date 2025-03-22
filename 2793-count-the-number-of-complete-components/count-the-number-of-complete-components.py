class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        hm = defaultdict(int)
        
        for v in range(n):
            adj[v] = [v]
        
        for v1,v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        for v in range(n):
            neigh = tuple(sorted(adj[v]))
            hm[neigh] += 1
        # print(hm)
        res = 0
        for neigh, freq in hm.items():
            if len(neigh) == freq:
                res += 1
        return res