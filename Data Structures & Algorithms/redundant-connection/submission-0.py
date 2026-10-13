class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # 建立邻接表，开始时没有任何连接
        n = len(edges)
        adj = {i: [] for i in range(1, n + 1)}

        # DFS 判断是否可以从 node 到达 target
        def dfs(node, target, visited):

            # 如果已经找到目标，说明两点连通
            if node == target:
                return True

            # 标记当前节点已经访问
            visited.add(node)

            # 遍历当前节点的所有邻居
            for nei in adj[node]:

                # 没访问过才继续 DFS，避免在无向图中循环
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            # 所有路径都找不到 target
            return False

        # 按输入顺序逐条添加边
        for a, b in edges:

            # 如果 a 和 b 已经连通
            # 再添加这条边就会形成环
            if dfs(a, b, set()):
                return [a, b]

            # 没有形成环，就把边加入无向图
            adj[a].append(b)
            adj[b].append(a)