class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def dfs(i, path):
            if i == len(nums):
                res.add(tuple(path))
                return##遍历到完整的长度之后可以return

            # 选择当前元素
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

            # 不选择当前元素
            dfs(i + 1, path)

        dfs(0, [])

        return [list(x) for x in res]