import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # dist[i][j]：到达该格子的最小 effort
        dist = [[float("inf")] * cols for _ in range(rows)]
        dist[0][0] = 0

        # (当前路径的 effort, 行, 列)
        heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            effort, i, j = heapq.heappop(heap)

            # 已经找到更好的路线，跳过旧记录
            if effort > dist[i][j]:
                continue

            # 终点第一次被有效弹出，当前 effort 就是最小值
            if i == rows - 1 and j == cols - 1:
                return effort

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if not (0 <= ni < rows and 0 <= nj < cols):
                    continue

                diff = abs(heights[i][j] - heights[ni][nj])

                # 路径 effort 是沿途最大的高度差
                new_effort = max(effort, diff)

                if new_effort < dist[ni][nj]:
                    dist[ni][nj] = new_effort
                    heapq.heappush(heap, (new_effort, ni, nj))