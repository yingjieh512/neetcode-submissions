class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i]：剩下从 i 开始的石头，当前玩家能领先对方多少分
        # dp[n] = 0：没有石头时，后续分差为 0
        dp = [0] * (n + 1)

        # 依赖后面的状态，所以从右往左计算
        for i in range(n - 1, -1, -1):
            # 拿 1 块，一定可以
            take1 = stoneValue[i] - dp[i + 1]

            # 拿 2、3 块需要检查剩余数量
            # 不合法的选择设为负无穷，避免被 max 选中
            take2 = float("-inf")
            take3 = float("-inf")

            if i + 2 <= n:
                take2 = (
                    stoneValue[i] + stoneValue[i + 1]
                    - dp[i + 2]
                )

            if i + 3 <= n:
                take3 = (
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2]
                    - dp[i + 3]
                )

            # 本轮得分 - 对方在剩余局面中的优势
            dp[i] = max(take1, take2, take3)

        # dp[0] 是开局时 Alice 相对 Bob 的分差
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"