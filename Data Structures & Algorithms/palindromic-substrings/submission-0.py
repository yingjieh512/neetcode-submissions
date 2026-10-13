class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # dp[i][j] 表示 s[i:j+1] 是否是回文子串
        # 初始全部为 False
        dp = [[False] * n for _ in range(n)]

        # 记录回文子串数量
        count = 0

        # 从右往左遍历起点 i
        # 因为 dp[i][j] 依赖 dp[i+1][j-1]
        # 所以必须先计算 i+1，再计算 i
        for i in range(n - 1, -1, -1):

            # j 是子串的结束位置
            # 必须满足 j >= i
            for j in range(i, n):

                # 两端字符必须相同
                if s[i] == s[j]:

                    # 长度 <= 3 时，两端相同就一定是回文
                    # 长度 > 3 时，需要检查中间是不是回文
                    if j - i <= 2 or dp[i + 1][j - 1]:

                        # 当前子串是回文
                        dp[i][j] = True

                        # 回文子串数量加 1
                        count += 1

        return count