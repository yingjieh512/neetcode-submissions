class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)

        # dp[i][s]：使用前 i 块石头，能否恰好凑出重量 s
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True  # 不选石头，可以凑出 0

        for i in range(1, n + 1):
            w = stones[i - 1]  # 当前石头的重量

            for s in range(target + 1):
                # 不选当前石头
                dp[i][s] = dp[i - 1][s]

                # 选当前石头，要求前面的石头能凑出 s - w
                if s >= w:
                    dp[i][s] = dp[i][s] or dp[i - 1][s - w]

        # 从一半往下找，找到能凑出的最大重量
        for best in range(target, -1, -1):
            if dp[n][best]:
                return total - 2 * best