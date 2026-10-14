
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # s1 和 s2 的长度之和必须等于 s3
        # 否则不可能组成 s3
        if m + n != len(s3):
            return False

        # dp[i][j] 表示：
        # s1 前 i 个字符 + s2 前 j 个字符
        # 能否交错组成 s3 前 i+j 个字符
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 两个空字符串可以组成空字符串
        dp[0][0] = True

        # 遍历 s1 和 s2 的所有前缀组合
        for i in range(m + 1):
            for j in range(n + 1):

                # 初始状态已经设置为 True
                if i == 0 and j == 0:
                    continue

                # 情况 1：当前字符从 s1 中取
                if i > 0:
                    if s1[i - 1] == s3[i + j - 1]:
                        if dp[i - 1][j]:
                            dp[i][j] = True

                # 情况 2：当前字符从 s2 中取
                if j > 0:
                    if s2[j - 1] == s3[i + j - 1]:
                        if dp[i][j - 1]:
                            dp[i][j] = True

        # 判断两个字符串能否组成完整的 s3
        return dp[m][n]
