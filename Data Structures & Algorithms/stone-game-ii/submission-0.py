class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # dp[i][M]：剩下从 i 开始的石头、参数为 M 时，
        # 当前玩家最终能领先对方多少分
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # dp[n][M] = 0：没有石头，后续分差为 0
        # 依赖更靠后的位置，所以从后往前计算
        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                dp[i][M] = float("-inf")
                taken = 0

                # 尝试拿 X 堆，不能超过 2M，也不能超过剩余堆数
                for X in range(1, min(2 * M, n - i) + 1):
                    # 比上次尝试多拿一堆，累加本轮得分
                    taken += piles[i + X - 1]

                    # 拿完后，轮到对方，新 M = max(M, X)
                    # 自己的分差 = 本轮得分 - 对方的后续优势
                    dp[i][M] = max(
                        dp[i][M],
                        taken - dp[i + X][max(M, X)]
                    )

        # 初始 Alice 先手，M = 1
        # 总分 + Alice 与 Bob 的分差 = 2 × Alice 的得分
        return (sum(piles) + dp[0][1]) // 2