class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hm = {}
        i = 0
        for eq1, eq2 in equations:
            if eq1 not in hm:
                hm[eq1] = i
                i+=1
            if eq2 not in hm:
                hm[eq2] = i
                i+=1

        # print(hm)
        adj = [[0]*i for _ in range(i)]
        j = 0
        for eq1, eq2 in equations:
            adj[hm[eq1]][hm[eq2]] = values[j]
            adj[hm[eq2]][hm[eq1]] = 1/values[j]
            j += 1

        # print(adj)

        def dfs(src,dst,cur,visited,temp):
            if src in visited or dst in visited:
                return
            if src == dst:
                cur[0] = temp
                return cur[0]
            
            visited.add(src)
            for k in range(i):
                if adj[src][k] != 0:
                    dfs(k,dst,cur,visited,temp*adj[src][k])
            return cur
        
        res = []
        for q1, q2 in queries:
            if q1 not in hm or q2 not in hm:
                res.append(-1)
            elif q1 == q2:
                res.append(1)
            elif adj[hm[q1]][hm[q2]] != 0:
                res.append(adj[hm[q1]][hm[q2]])
            else:
                visited = set()
                cur = [-1]
                temp = 1
                dfs(hm[q1],hm[q2],cur,visited,temp)
                res.append(cur[0])

        # print(res)
        return res