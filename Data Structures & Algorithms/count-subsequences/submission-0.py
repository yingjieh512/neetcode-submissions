
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] 表示：
        # 从 s 的前 i 个字符中，
        # 选出等于 t 的前 j 个字符的子序列数量
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # t 为空时，只有一种匹配方式：
        # 从 s 中什么字符都不选
        for i in range(m + 1):
            dp[i][0] = 1

        # 遍历 s 的每个前缀
        for i in range(1, m + 1):

            # 遍历 t 的每个前缀
            for j in range(1, n + 1):

                # 当前两个字符相同
                if s[i - 1] == t[j - 1]:

                    # 不使用 s[i-1]：
                    # dp[i-1][j]
                    #
                    # 使用 s[i-1]：
                    # dp[i-1][j-1]
                    #
                    # 两种选择的数量相加
                    dp[i][j] = (
                        dp[i - 1][j]
                        + dp[i - 1][j - 1]
                    )

                else:
                    # 字符不同，只能跳过 s[i-1]
                    dp[i][j] = dp[i - 1][j]

        # 返回使用整个 s 匹配整个 t 的方式数量
        return dp[m][n]
