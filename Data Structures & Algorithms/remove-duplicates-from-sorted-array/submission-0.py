class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow 指向已经去重部分的最后一个元素
        slow = 0

        # fast 从第二个元素开始遍历
        for fast in range(1, len(nums)):

            # 如果找到一个不同的数字
            if nums[fast] != nums[slow]:

                # slow 向右移动一格
                slow += 1

                # 把新数字放到去重部分的末尾
                nums[slow] = nums[fast]

        # slow 是索引，所以唯一元素数量要加 1
        return slow + 1