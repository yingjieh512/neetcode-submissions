class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # 一棵树有 n 个节点，就必须恰好有 n - 1 条边
        # 如果边数不符合，直接返回 False
        if len(edges) != n - 1:
            return False

        # 建立邻接表，记录每个节点连接了哪些节点
        # 例如 adj[0] = [1, 2] 表示节点 0 连接节点 1 和 2
        adj = {i: [] for i in range(n)}

        # 无向图：a 连接 b，b 也连接 a
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # 记录已经访问过的节点，防止 DFS 重复访问
        visited = set()

        def dfs(node):
            # 如果节点已经访问过，就不需要再搜索
            if node in visited:
                return

            # 标记当前节点已经访问
            visited.add(node)

            # 遍历当前节点的所有邻居
            for nei in adj[node]:
                # 递归访问邻居，寻找所有连通的节点
                dfs(nei)

        # 从节点 0 开始 DFS
        # 如果图是连通的，就应该能够访问全部 n 个节点
        dfs(0)

        # 前面已经检查了边数等于 n - 1
        # 这里只需要检查是否所有节点都连通
        # n - 1 条边 + 全部连通 = 一棵合法的树
        return len(visited) == n