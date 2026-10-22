from collections import deque

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo(conditions):
            graph = [[] for _ in range(k + 1)]
            indegree = [0] * (k + 1)

            # 建图
            for a, b in conditions:
                graph[a].append(b)
                indegree[b] += 1

            # 所有入度为 0 的节点
            q = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            order = []

            # BFS
            while q:
                node = q.popleft()
                order.append(node)

                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            # 如果有环，就无法完成排序
            if len(order) != k:
                return []

            return order

        # 分别对行、列排序
        row_order = topo(rowConditions)
        col_order = topo(colConditions)

        if not row_order or not col_order:
            return []

        # 记录每个数字的行、列位置
        row_pos = {}
        col_pos = {}

        for i in range(k):
            row_pos[row_order[i]] = i
            col_pos[col_order[i]] = i

        # 构建矩阵
        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix