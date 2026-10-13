
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x] 表示：使用已经处理过的硬币面额，
        # 凑出金额 x 的不同组合数量
        dp = [0] * (amount + 1)

        # 凑出金额 0 有一种方法：不使用任何硬币
        dp[0] = 1

        # 外层遍历硬币面额
        # 确保每种组合只会被计算一次，不考虑排列顺序
        for coin in coins:

            # 从 coin 开始，依次计算每个金额的组合数量
            # 正序遍历允许当前硬币被重复使用
            for x in range(coin, amount + 1):

                # 不使用当前硬币的组合已包含在 dp[x] 中
                # 再加上使用当前硬币的新增组合数量
                dp[x] += dp[x - coin]

        # 返回凑出目标金额的全部组合数量
        return dp[amount]
