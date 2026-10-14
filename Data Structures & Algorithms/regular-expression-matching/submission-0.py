
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] 表示：
        # s 的前 i 个字符
        # 能否被 p 的前 j 个字符完整匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 空字符串可以匹配空模式
        dp[0][0] = True

        # i 从 0 开始，因为空字符串也可能匹配 a*、a*b* 等
        for i in range(m + 1):
            for j in range(1, n + 1):

                # 情况 1：当前模式字符是 *
                if p[j - 1] == "*":

                    # 选择 A：* 匹配 0 次
                    # 跳过 * 和它前面的字符
                    dp[i][j] = dp[i][j - 2]

                    # 选择 B：* 匹配至少 1 次
                    # 首先检查 s 是否还有字符
                    if i > 0:

                        # * 前面的字符可以匹配当前 s 字符
                        if p[j - 2] == s[i - 1] or p[j - 2] == ".":

                            # 消耗 s 当前字符，但保留整个模式
                            # 因为 * 还可以继续匹配更多字符
                            dp[i][j] = (
                                dp[i][j] or dp[i - 1][j]
                            )

                # 情况 2：普通字符或者 .
                else:
                    if i > 0:

                        # 当前两个字符可以匹配
                        if p[j - 1] == s[i - 1] or p[j - 1] == ".":

                            # 两边各消耗一个字符
                            dp[i][j] = dp[i - 1][j - 1]

        # 返回两个完整字符串是否匹配
        return dp[m][n]
