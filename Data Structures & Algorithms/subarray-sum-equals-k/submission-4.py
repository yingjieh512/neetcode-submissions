class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key: 之前出现过的前缀和
        # value: 这个前缀和出现过多少次
        count = {0: 1}

        # 当前前缀和
        prefix_sum = 0

        # 满足条件的子数组数量
        res = 0

        for num in nums:
            # 更新当前前缀和
            prefix_sum += num

            # 需要寻找的历史前缀和
            target = prefix_sum - k

            # 如果之前出现过 target，
            # 每出现一次，就对应一个和为 k 的子数组
            if target in count:
                res += count[target]

            # 记录当前前缀和出现的次数
            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return res