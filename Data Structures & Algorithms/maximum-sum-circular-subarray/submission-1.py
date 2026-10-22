class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]

        # 以当前元素结尾的最大、最小子数组和
        max_end = min_end = nums[0]

        # 全局最大、最小子数组和
        max_sum = min_sum = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            total += x

            # 从当前数字重新开始，或者接上前面的连续段
            max_end = max(x, max_end + x)
            min_end = min(x, min_end + x)

            max_sum = max(max_sum, max_end)
            min_sum = min(min_sum, min_end)

        # 全是负数时，不能通过删掉整个数组得到空数组
        if max_sum < 0:
            return max_sum

        # 不跨首尾，或者跨首尾（去掉最小连续段）
        return max(max_sum, total - min_sum)