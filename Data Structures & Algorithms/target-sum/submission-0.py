
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[sum] 表示：
        # 使用目前已经处理过的数字，
        # 得到总和 sum 的方式数量
        dp = {0: 1}

        # 依次处理 nums 中的每一个数字
        for num in nums:

            # 创建下一轮的 DP
            # 不能直接修改 dp，否则可能重复使用当前数字
            new_dp = {}

            # 遍历之前所有可能的 sum
            for s, count in dp.items():

                # 第一种选择：给当前数字加正号
                plus = s + num

                # 所有之前得到 s 的方式，
                # 都可以通过 +num 得到 plus
                new_dp[plus] = new_dp.get(plus, 0) + count

                # 第二种选择：给当前数字加负号
                minus = s - num

                # 所有之前得到 s 的方式，
                # 都可以通过 -num 得到 minus
                new_dp[minus] = new_dp.get(minus, 0) + count

            # 更新 DP，进入下一个数字
            dp = new_dp

        # 所有数字处理完后，
        # 返回最终得到 target 的方式数量
        # 如果 target 不存在，则返回 0
        return dp.get(target, 0)
