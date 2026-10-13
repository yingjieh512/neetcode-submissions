class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # 建立邻接表，记录每个节点连接了哪些节点
        adj = {i: [] for i in range(n)}

        # 无向图：a 连接 b，b 也连接 a
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # 记录已经访问过的节点，避免重复访问
        visited = set()

        def dfs(node):
            # 如果已经访问过，直接返回
            if node in visited:
                return

            # 标记当前节点已经访问
            visited.add(node)

            # 继续访问当前节点的所有邻居
            for nei in adj[node]:
                dfs(nei)

        # 记录 Connected Components 的数量
        count = 0

        # 遍历所有节点，包括没有任何边的孤立节点
        for i in range(n):

            # 如果当前节点没访问过
            # 说明发现了一个新的 Connected Component
            if i not in visited:

                # 从当前节点开始 DFS
                # 一次 DFS 会访问这个 Component 中的所有节点
                dfs(i)

                # 找到一个新的 Connected Component
                count += 1

        return count