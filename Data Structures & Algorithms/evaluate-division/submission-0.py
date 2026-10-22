from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(list)

        # a / b = value，反过来 b / a = 1 / value
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def bfs(start, target):
            # 没出现过的变量无法求值，包括未知变量除以自己
            if start not in graph or target not in graph:
                return -1.0

            # (当前变量, start / 当前变量的值)
            queue = deque([(start, 1.0)])
            visited = {start}

            while queue:
                current, product = queue.popleft()

                if current == target:
                    return product

                for neighbor, weight in graph[current]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)

                    # start/current × current/neighbor
                    # = start/neighbor
                    queue.append((neighbor, product * weight))

            # 两个变量之间没有路径
            return -1.0

        return [bfs(a, b) for a, b in queries]