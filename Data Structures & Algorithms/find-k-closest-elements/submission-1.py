class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # 左右指针，初始包含整个数组
        left = 0
        right = len(arr) - 1

        # 只要窗口大小超过 k，就删除一个元素
        while right - left + 1 > k:

            # 比较左右端点到 x 的距离
            if abs(arr[left] - x) > abs(arr[right] - x):

                # 左边距离更远，删除左边
                left += 1

            else:
                # 右边距离更远，或者两边距离相等
                # 距离相等时，要保留更小的数字
                # 所以删除右边
                right -= 1

        # 返回最终剩下的 k 个元素
        return arr[left:right + 1]