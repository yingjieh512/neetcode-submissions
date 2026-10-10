class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, path, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(candidates) or total > target:
                return

            # 选择当前数字
            path.append(candidates[i])
            dfs(i + 1, path, total + candidates[i])
            path.pop()

            # 不选择当前数字
            # 跳过后面所有相同的数字
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, path, total)

        dfs(0, [], 0)
        return res