class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        # dp[i] 表示必须以 nums[i] 结尾的
        # 最长严格递增子序列的长度
        # 每个数字自己都能形成长度为 1 的子序列
        dp = [1] * n

        # 遍历每个数字，计算以它结尾的 LIS
        for i in range(n):

            # 检查 nums[i] 前面的所有数字
            for j in range(i):

                # 只有前面的数字比当前数字小时
                # 才能把 nums[i] 接在 nums[j] 后面
                if nums[j] < nums[i]:

                    # 两种选择：
                    # 1. 保留当前 dp[i]
                    # 2. 接在以 nums[j] 结尾的子序列后面，长度 +1
                    dp[i] = max(dp[i], dp[j] + 1)

        # 最长递增子序列不一定以最后一个数字结尾
        # 所以返回所有 dp 中的最大值
        return max(dp)