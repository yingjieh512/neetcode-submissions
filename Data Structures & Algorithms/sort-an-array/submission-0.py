class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(arr):
            # Base Case：只有 0 或 1 个元素时，已经有序
            if len(arr) <= 1:
                return arr

            # 第一步：将数组分成左右两半
            mid = len(arr) // 2

            # 递归排序左半部分
            left = mergeSort(arr[:mid])

            # 递归排序右半部分
            right = mergeSort(arr[mid:])

            # 第二步：合并两个有序数组
            result = []

            # i 指向 left 的当前元素
            # j 指向 right 的当前元素
            i = 0
            j = 0

            # 两边都还有元素时，比较较小值
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # 如果 left 还有剩余元素，全部加入
            while i < len(left):
                result.append(left[i])
                i += 1

            # 如果 right 还有剩余元素，全部加入
            while j < len(right):
                result.append(right[j])
                j += 1

            # 返回当前已经排序好的数组
            return result

        return mergeSort(nums)