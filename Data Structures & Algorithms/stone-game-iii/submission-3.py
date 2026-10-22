class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i]：剩下从 i 开始的石头，当前玩家最终能领先对方多少分
        # dp[n] = 0：没有石头时，后续双方得分差为 0
        dp = [0] * (n + 1)

        # dp[i] 依赖后面的状态，所以从右往左计算
        for i in range(n - 1, -1, -1):
            total = 0  # 当前这一轮拿到的石头总分

            # 必须拿石头，且最优分差也可能为负，所以不能初始化为 0
            dp[i] = float("-inf")

            # 分别尝试拿 1、2、3 块石头
            for take in range(1, 4):
                if i + take > n:
                    break  # 剩余石头不够拿

                # 比上一次尝试多拿一块，累加这一块的分数
                total += stoneValue[i + take - 1]

                # 拿完后轮到对方，从 i + take 开始
                # dp[i + take] 是对方在剩余局面中的优势
                # 因此自己的最终分差 = 本轮得分 - 对方的后续优势
                dp[i] = max(dp[i], total - dp[i + take])

        # 最开始的当前玩家是 Alice
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"