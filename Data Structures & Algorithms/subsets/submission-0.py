class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # 不选择 nums[i]
            dfs(i + 1)

            # 选择 nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # 回溯
            subset.pop()

        dfs(0)
        return res