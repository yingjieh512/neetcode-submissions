class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            total = 0
            dp[i] = float("-inf")

            for take in range(1, 4):
                if i + take > n:
                    break

                total += stoneValue[i + take - 1]
                dp[i] = max(dp[i], total - dp[i + take])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
