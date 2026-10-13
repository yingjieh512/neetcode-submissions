class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 计算总和
        total = sum(nums)

        # 总和为奇数，无法平分
        if total % 2 != 0:
            return False

        # 每个 subset 需要达到的目标总和
        target = total // 2

        # dp[s] 表示是否能组成总和 s
        dp = [False] * (target + 1)

        # 不选择任何数字就能组成 0
        dp[0] = True

        # 遍历数组中的每个数字
        for num in nums:

            # 必须从右向左遍历
            # 防止同一个数字在一轮中被重复使用
            for s in range(target, num - 1, -1):

                # 不选 num：保留原来的 dp[s]
                # 选 num：检查之前能否组成 s - num
                dp[s] = dp[s] or dp[s - num]

        # 判断能否组成目标总和
        return dp[target]