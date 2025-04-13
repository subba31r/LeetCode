class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(rooms,start,visited=None):
            if visited is None:
                visited = set()
            visited.add(start)

            for next in set(rooms[start])-visited:
                dfs(rooms,next,visited)
            return visited
        return len(dfs(rooms,0)) == len(rooms)
        # visited = [False, False, False, False]
        # 0 -> 1, 3
        # Queue = [1,3] visited = [True, False, False, False]
        # 1 -> 3, 0, 1
        # Queue = [3,3,0,1] visited = [True, True, False, False]
        # Queue = [], visited = [True, True, False, True]
        # 2 -> 2
        # 3 -> 0