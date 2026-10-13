class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # maxProd：以当前位置结尾的最大乘积
        # minProd：以当前位置结尾的最小乘积
        # 初始时只有第一个元素
        maxProd = nums[0]
        minProd = nums[0]

        # res：整个数组中找到的最大乘积
        res = nums[0]

        # 从第二个元素开始遍历
        for i in range(1, len(nums)):
            num = nums[i]

            # 计算以当前元素结尾的三种可能
            # 1. 只选择当前元素，重新开始子数组
            # 2. 乘以前一个位置的最大乘积
            # 3. 乘以前一个位置的最小乘积
            a = num
            b = num * maxProd
            c = num * minProd

            # 更新以当前元素结尾的最大、最小乘积
            maxProd = max(a, b, c)
            minProd = min(a, b, c)

            # 更新全局最大乘积
            res = max(res, maxProd)

        return res