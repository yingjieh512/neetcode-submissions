class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 1. 找 rotating point / 最小值
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 2. 判断 target 应该在哪一段
        if nums[pivot] <= target <= nums[n - 1]:
            left = pivot
            right = n - 1
        else:
            left = 0
            right = pivot - 1

        # 3. 普通 binary search
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1