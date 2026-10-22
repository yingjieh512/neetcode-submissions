class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        path=[]
        def dfs():
            if len(path) == len(nums):
                res.append(path[:])  # 保存副本，避免后续撤回影响答案
                return

            # 当前这一位，相同数字只尝试一次
            seen = set()

            for i in range(len(nums)):
                if used[i] or nums[i] in seen:
                    continue

                seen.add(nums[i])

                # 选择当前位置的数字
                path.append(nums[i])
                used[i] = True

                # 去填写下一位
                dfs()

                # 撤回，让循环尝试当前这一位的其他选择
                path.pop()
                used[i] = False
        dfs()
        return res


                