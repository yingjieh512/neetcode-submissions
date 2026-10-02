class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            # 选择 nums[i]
            subset.append(nums[i])
            dfs(i, total + nums[i])   # 还是 i，可以重复选择
            subset.pop()

            # 不选择 nums[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return res