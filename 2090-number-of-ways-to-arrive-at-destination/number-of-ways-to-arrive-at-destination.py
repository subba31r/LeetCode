import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        adj = [[] for _ in range(n)]

        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        hq = [(0,0)]
        dist = [float('inf')]*n
        dist[0] = 0
        path_count = [0] * n
        path_count[0] = 1
        while hq:
            distance, u = heapq.heappop(hq)
            for v, wt in adj[u]:
                if distance + wt < dist[v]:
                    dist[v] = distance + wt
                    path_count[v] = path_count[u]
                    heapq.heappush(hq,(dist[v],v))
                elif dist[v] == distance + wt:
                    path_count[v] = (path_count[v]+path_count[u])%MOD
        
        return path_count[n-1]