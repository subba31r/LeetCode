from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        res = [0] * len(queries)

        sorted_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        min_heap = []
        visited = [[False] * n for _ in range(m)]

        total = 0
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True 

        for val, idx in sorted_queries:
            while min_heap and min_heap[0][0] < val:
                cellVal, i, j = heapq.heappop(min_heap)
                total += 1
                for r, c in directions:
                    dr, dc = i + r, j + c
                    if 0 <= dr < m and 0 <= dc < n and not visited[dr][dc]:
                        visited[dr][dc] = True
                        heapq.heappush(min_heap, (grid[dr][dc], dr, dc))
            res[idx] = total

        return res
