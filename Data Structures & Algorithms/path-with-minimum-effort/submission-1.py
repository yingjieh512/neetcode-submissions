import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        graph = defaultdict(list)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 1. 建图，节点用 (行, 列) 表示
        for i in range(rows):
            for j in range(cols):
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < rows and 0 <= nj < cols:
                        diff = abs(heights[i][j] - heights[ni][nj])
                        graph[(i, j)].append((ni, nj, diff))

        # 2. Dijkstra
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            effort, i, j = heapq.heappop(heap)

            if effort > dist[i][j]:
                continue

            if i == rows - 1 and j == cols - 1:
                return effort

            # 直接读取已经建好的边
            for ni, nj, diff in graph[(i, j)]:
                new_effort = max(effort, diff)

                if new_effort < dist[ni][nj]:
                    dist[ni][nj] = new_effort
                    heapq.heappush(heap, (new_effort, ni, nj))