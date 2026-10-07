from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        left = 0

        for right in range(len(nums)):

            # 保持 deque 对应的值递减
            while q and nums[q[-1]] <= nums[right]:
                q.pop()

            q.append(right)

            # 删除已经离开窗口的元素
            if q[0] < left:
                q.popleft()

            # 窗口达到 k
            if right - left + 1 == k:
                res.append(nums[q[0]])
                left += 1

        return res