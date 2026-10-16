class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        i = 0

        # 只需要检查尚未排序的区域
        while i <= right:

            if nums[i] == 0:
                # 0 放到左边
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1

            elif nums[i] == 1:
                # 1 留在中间
                i += 1

            else:
                # 2 放到右边
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1

                # 这里不移动 i
                # 因为交换过来的元素还没检查