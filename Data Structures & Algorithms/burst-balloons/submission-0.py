
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 在左右两端添加 1，方便计算边界情况
        arr = [1] + nums + [1]
        n = len(nums)

        # dp[l][r] 表示：
        # 戳破 l 和 r 之间所有气球的最大金币数量
        # 注意：不戳破边界 l 和 r
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # length 表示两个边界下标之间的距离
        # 最小距离是 2，代表中间只有一个气球
        # 最大距离是 n+1，代表包含所有原始气球
        for length in range(2, n + 2):

            # 枚举左边界
            for l in range(n + 2 - length):

                # 根据左边界和区间长度确定右边界
                r = l + length

                # 枚举最后一个被戳破的气球 k
                # k 必须严格位于 l 和 r 之间
                for k in range(l + 1, r):

                    # 左边区间：(l, k)
                    left = dp[l][k]

                    # 右边区间：(k, r)
                    right = dp[k][r]

                    # 当 k 最后被戳破时，
                    # 左右邻居一定是 l 和 r
                    coins = arr[l] * arr[k] * arr[r]

                    # 选择能够获得最多金币的最后一个气球
                    dp[l][r] = max(
                        dp[l][r],
                        left + right + coins
                    )

        # 两端添加的 1 不需要戳破
        # 返回戳破所有原始气球的最大金币
        return dp[0][n + 1]
