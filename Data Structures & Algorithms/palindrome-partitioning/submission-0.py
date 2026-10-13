class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []   # 存储所有合法的分割结果
        path = []  # 存储当前正在尝试的分割方式

        # 判断字符串是否为回文
        def isPalindrome(sub):
            return sub == sub[::-1]

        # start 表示下一段子字符串从哪个位置开始
        def dfs(start):

            # Base case:
            # 如果已经处理完整个字符串
            # 说明当前 path 是一种合法分割
            if start == len(s):
                res.append(path.copy())
                return

            # 枚举当前子字符串的所有可能结束位置
            for end in range(start + 1, len(s) + 1):

                # Python 切片左闭右开
                # 从 start 切到 end - 1
                sub = s[start:end]

                # 如果当前子字符串不是回文，跳过
                if not isPalindrome(sub):
                    continue

                # 1. 做选择
                # 当前子字符串是回文，加入 path
                path.append(sub)

                # 2. 递归
                # 从 end 开始继续分割剩余字符串
                dfs(end)

                # 3. 撤销选择（回溯）
                # 尝试其他切割位置
                path.pop()

        dfs(0)
        return res