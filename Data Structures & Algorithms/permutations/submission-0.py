class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        path = []

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                # 选择
                path.append(num)
                used.add(num)

                dfs()

                # 回溯，撤销选择
                path.pop()
                used.remove(num)

        dfs()
        return res