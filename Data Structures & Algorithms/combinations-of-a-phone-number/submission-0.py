class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # 每个数字对应的字母
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []   # 存储所有组合
        path = []  # 当前正在构造的组合

        # i 表示当前处理第几个数字
        def dfs(i):

            # 所有数字都已经处理完毕
            if i == len(digits):
                res.append("".join(path))
                return

            # 获取当前数字对应的所有字母
            letters = mapping[digits[i]]

            # 尝试当前数字对应的每一个字母
            for char in letters:

                # 1. 选择一个字母
                path.append(char)

                # 2. 递归处理下一个数字
                dfs(i + 1)

                # 3. 回溯，撤销当前选择
                path.pop()

        dfs(0)
        return res