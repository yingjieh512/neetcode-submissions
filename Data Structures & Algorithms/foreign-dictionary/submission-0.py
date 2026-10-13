class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # 建立邻接表
        # 每个字母都是一个节点
        # adj[a] 记录必须排在 a 后面的字母
        adj = {c: set() for word in words for c in word}

        # 比较相邻的单词，建立字母之间的先后关系
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # 如果前一个单词更长，而且后一个是它的前缀
            # 例如 "abc" 排在 "ab" 前面，不符合字典顺序
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # 找到两个单词第一个不同的字母
            for j in range(min(len(w1), len(w2))):

                if w1[j] != w2[j]:

                    # w1[j] 必须排在 w2[j] 前面
                    # 因此建立有向边
                    adj[w1[j]].add(w2[j])

                    # 只需要第一个不同的字母
                    break

        # visited 记录每个字母的 DFS 状态
        # 不存在：从未访问
        # True：正在当前 DFS 路径中
        # False：已经完成 DFS
        visited = {}

        # 记录拓扑排序结果
        res = []

        def dfs(c):

            # 如果访问过这个字母
            if c in visited:
                # True 表示当前递归路径中重复遇到它，存在环
                # False 表示已经处理完，不需要重复访问
                return visited[c]

            # 标记为正在访问
            visited[c] = True

            # 访问所有必须排在当前字母后面的字母
            for nei in adj[c]:
                if dfs(nei):
                    return True

            # 当前字母及其后续节点全部处理完成
            visited[c] = False

            # DFS 回溯时加入结果
            res.append(c)

            return False

        # 对每个字母进行 DFS
        for c in adj:
            # 如果发现环，就无法确定合法的字母顺序
            if dfs(c):
                return ""

        # 因为 DFS 是后序添加，所以需要反转
        res.reverse()

        return "".join(res)