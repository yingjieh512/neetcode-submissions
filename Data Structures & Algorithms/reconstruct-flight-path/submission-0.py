from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # 建立邻接表
        # 每个出发机场对应它可以飞往的目的地
        adj = defaultdict(list)

        # 反向排序
        # 这样之后使用 pop()，每次取到的是字典序最小的机场
        for a, b in sorted(tickets, reverse=True):
            adj[a].append(b)

        # 记录最终路径，但是按照逆序添加
        res = []

        def dfs(airport):

            # 只要当前机场还有没使用的机票，就继续 DFS
            while adj[airport]:

                # 取出字典序最小的目的地
                # pop() 同时表示这张机票已经使用过
                nei = adj[airport].pop()

                # 继续从目的地出发
                dfs(nei)

            # 当前机场已经没有剩余机票可以使用
            # 这时才把机场加入路径
            res.append(airport)

        # 必须从 JFK 开始
        dfs("JFK")

        # 因为 DFS 是倒序添加机场，所以最后需要反转
        return res[::-1]