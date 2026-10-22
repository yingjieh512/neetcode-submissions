class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # 保存原始 index，因为排序会改变顺序
        for i in range(len(edges)):
            edges[i].append(i)

        # 按照 weight 排序
        edges.sort(key=lambda x: x[2])

        # Kruskal: 可以跳过某条边，也可以强制加入某条边
        def mst(skip=-1, force=-1):
            parent = list(range(n))
            size = [1] * n

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(a, b):
                pa = find(a)
                pb = find(b)

                if pa == pb:
                    return False

                if size[pa] < size[pb]:
                    pa, pb = pb, pa

                parent[pb] = pa
                size[pa] += size[pb]
                return True

            cost = 0
            count = 0

            # 强制选择某条边
            if force != -1:
                u, v, w, idx = edges[force]
                union(u, v)
                cost += w
                count += 1

            # 正常运行 Kruskal
            for i, (u, v, w, idx) in enumerate(edges):

                if i == skip or i == force:
                    continue

                if union(u, v):
                    cost += w
                    count += 1

            if count != n - 1:
                return float('inf')

            return cost

        original = mst()

        critical = []
        pseudo = []

        for i in range(len(edges)):

            if mst(skip=i) > original:
                critical.append(edges[i][3])

            elif mst(force=i) == original:
                pseudo.append(edges[i][3])

        return [critical, pseudo]