
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # m 是 word1 的长度，n 是 word2 的长度
        m, n = len(word1), len(word2)

        # dp[i][j] 表示：
        # 将 word1 的前 i 个字符
        # 转换成 word2 的前 j 个字符的最少操作次数
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 如果 word2 为空：
        # 只能把 word1 前 i 个字符全部删除
        for i in range(m + 1):
            dp[i][0] = i

        # 如果 word1 为空：
        # 只能插入 word2 的前 j 个字符
        for j in range(n + 1):
            dp[0][j] = j

        # 从短字符串开始，逐渐计算更长前缀的答案
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # 两个前缀的最后一个字符相同
                # 不需要额外操作
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    # 删除 word1 的最后一个字符
                    delete = dp[i - 1][j]

                    # 插入 word2 的最后一个字符
                    insert = dp[i][j - 1]

                    # 替换 word1 的最后一个字符
                    replace = dp[i - 1][j - 1]

                    # 选择三种操作中代价最小的一种
                    # +1 表示执行当前这一次编辑
                    dp[i][j] = 1 + min(
                        delete, insert, replace
                    )

        # 返回两个完整字符串之间的编辑距离
        return dp[m][n]
