from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:

        # 建有向图：a 是 b 的先修课，连接 a → b
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        # reachable[u][v]：能否从 u 到达 v
        reachable = [[False] * numCourses for _ in range(numCourses)]

        # 从每门课程出发，分别做一次 BFS
        for start in range(numCourses):
            queue = deque([start])
            visited = {start}

            while queue:
                course = queue.popleft()

                for neighbor in graph[course]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    reachable[start][neighbor] = True
                    queue.append(neighbor)

        # 每个查询直接查表
        return [reachable[u][v] for u, v in queries]