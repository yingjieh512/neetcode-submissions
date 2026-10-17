class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        res=0
        minlen=float("inf")
        for right in range(len(nums)):
            res+=nums[right]
            # 只要窗口总和达到 target，就尝试缩小窗口
            while res >= target:
                # 记录当前满足条件的窗口长度
                minlen = min(minlen, right - left + 1)

                # 先移除左边界的元素
                res -= nums[left]

                # 再移动左指针
                left += 1

        # 如果没有找到符合条件的子数组，返回 0
        if minlen == float('inf'):
            return 0
        return minlen
