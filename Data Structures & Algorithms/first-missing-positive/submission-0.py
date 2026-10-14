class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):

            # 只有 1 到 n 之间的数字才需要放到正确的位置
            # nums[i] - 1 就是当前数字应该去的位置
            # 如果目标位置已经是这个数字，就不需要交换
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:

                # 计算当前数字应该放的位置
                correct = nums[i] - 1

                # 把当前数字交换到正确的位置
                nums[i], nums[correct] = nums[correct], nums[i]

        # 检查每个位置是否放了正确的数字
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果 1 到 n 都存在，答案就是 n + 1
        return n + 1