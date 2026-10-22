from collections import deque
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n

        # 建立无向图，记录每个节点的邻居数量
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # 第一层叶子：只有一个邻居
        queue = deque(i for i in range(n) if degree[i] == 1)
        remaining = n

        while remaining > 2:
            # 固定本层数量，新加入的叶子留到下一轮处理
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    # 已经删除的节点不再处理
                    if degree[neighbor] == 0:
                        continue

                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

                degree[leaf] = 0

        return list(queue)