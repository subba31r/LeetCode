class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited =[False]*n

        def dfs(isConnected, start, visited):
            if visited[start] == True:
                return
            visited[start] = True
            for i in range(n):
                if isConnected[start][i] == 1:
                    dfs(isConnected,i,visited)
            return visited
        
        for i in range(n):
            if visited[i] == False:
                visited = dfs(isConnected,i,visited)
                count += 1
        return count