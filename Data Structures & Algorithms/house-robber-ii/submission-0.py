class Solution:
    def rob(self, nums: List[int]) -> int:

        # 如果只有一间房子，直接抢这一间
        if len(nums) == 1:
            return nums[0]

        # House Robber I 的解法
        # 计算一排房子最多能抢多少钱
        def helper(houses):

            # rob1 表示前两步的最优结果
            # rob2 表示前一步的最优结果
            rob1, rob2 = 0, 0

            for money in houses:

                # 两种选择：
                # 1. 抢当前房子：money + rob1
                # 2. 不抢当前房子：rob2
                current = max(money + rob1, rob2)

                # 更新 DP 状态，向后移动一间房
                rob1 = rob2
                rob2 = current

            # 返回这一排房子能抢到的最大金额
            return rob2

        # 情况 1：不考虑最后一间房子
        case1 = helper(nums[:-1])

        # 情况 2：不考虑第一间房子
        case2 = helper(nums[1:])

        # 取两种情况中最大的结果
        return max(case1, case2)