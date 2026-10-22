class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        # dp[i][j]：只剩下区间 [i, j] 时，
        # 当前玩家最终能领先对方多少分
        for i in range(n):
            dp[i][i] = piles[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],  # 拿左边
                    piles[j] - dp[i][j - 1]   # 拿右边
                )
        # 开局的当前玩家是 Alice
        return dp[0][n - 1] > 0