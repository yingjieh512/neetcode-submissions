class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(len(nums)):

            # 如果之前的窗口已经超过 k 个索引距离
            # 删除最左边的元素，保持窗口范围合法
            if right - left > k:
                window.remove(nums[left])
                left += 1

            # 检查当前数字是否已经在窗口中
            # 如果存在，说明两个相同数字的索引距离 <= k
            if nums[right] in window:
                return True

            # 当前数字加入窗口
            window.add(nums[right])

        return False