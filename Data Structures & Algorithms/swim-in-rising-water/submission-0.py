import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # 网格大小为 n × n
        n = len(grid)

        # 最小堆：(到达当前位置所需的最小时间, 行, 列)
        # 一开始位于 (0,0)，最早进入时间是 grid[0][0]
        minHeap = [(grid[0][0], 0, 0)]

        # 记录已经确定最优时间的格子
        visited = set()

        while minHeap:

            # 每次取出当前所需时间最小的格子
            time, r, c = heapq.heappop(minHeap)

            # 如果这个格子已经处理过，就跳过
            if (r, c) in visited:
                continue

            # 标记已经访问
            visited.add((r, c))

            # 到达右下角，当前 time 就是最早到达时间
            if r == n - 1 and c == n - 1:
                return time

            # 遍历上下左右四个方向
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                nr = r + dr
                nc = c + dc

                # 检查是否在网格内，并且没有访问过
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:

                    # 到达邻居需要的时间：
                    # 当前路径所需时间和邻居高度的最大值
                    newTime = max(time, grid[nr][nc])

                    # 将新路径加入最小堆
                    heapq.heappush(minHeap, (newTime, nr, nc))