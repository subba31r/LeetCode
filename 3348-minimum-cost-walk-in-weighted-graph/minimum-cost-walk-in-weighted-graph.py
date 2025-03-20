class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append((e[1],e[2]))
            adj[e[1]].append((e[0],e[2]))
        
        visited = [False]*n
        components = [0]*n #to store componentID of each node
        componentCost = []
        componentId = 0

        for node in range(n):
            if not visited[node]:
                componentCost.append(self.getComponentCost(node, adj, visited,components,componentId))
                componentId += 1
        
        res = []
        for start, end in query:
            if components[start] == components[end]:
                res.append(componentCost[components[start]])
            else:
                res.append(-1)
        return res
    
    def getComponentCost(self,node, adj, visited,components,componentId):
        components[node] = componentId
        visited[node] = True
        currentCost = -1
        for neigh, weight in adj[node]:
            currentCost &= weight
            if not visited[neigh]:
                currentCost &= self.getComponentCost(neigh, adj, visited,components,componentId)
        return currentCost
        