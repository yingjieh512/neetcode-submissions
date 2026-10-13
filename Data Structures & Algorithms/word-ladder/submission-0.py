from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # 如果目标单词不在 wordList 中，就无法转换
        if endWord not in wordList:
            return 0

        # 把起始单词也加入单词列表
        words = [beginWord] + wordList

        # 建立邻接表，记录每个单词可以转换到哪些单词
        adj = {word: [] for word in words}

        # 比较任意两个单词，判断是否恰好只差一个字母
        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                # 计算两个单词有几个位置的字母不同
                diff = 0

                for k in range(len(beginWord)):
                    if words[i][k] != words[j][k]:
                        diff += 1

                # 只有恰好一个字母不同时，才能建立连接
                if diff == 1:
                    adj[words[i]].append(words[j])
                    adj[words[j]].append(words[i])

        # BFS 队列：(当前单词, 转换序列中的单词数量)
        # 起点本身算一个单词，所以从 1 开始
        queue = deque([(beginWord, 1)])

        # 记录已经访问的单词，避免重复访问
        visited = {beginWord}

        while queue:
            # 取出当前单词和当前路径长度
            word, steps = queue.popleft()

            # 找到目标单词，返回最短转换序列长度
            if word == endWord:
                return steps

            # 遍历所有可以一步转换到的单词
            for nei in adj[word]:

                # 没有访问过才加入队列
                if nei not in visited:
                    visited.add(nei)

                    # 转换到下一个单词，长度加 1
                    queue.append((nei, steps + 1))

        # BFS 结束仍然无法到达目标单词
        return 0