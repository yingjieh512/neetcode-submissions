class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        # 遍历第一个字符串中的每一个字符
        # i 代表当前检查的字符位置
        for i in range(len(strs[0])):

            # 遍历剩余的所有字符串
            for s in strs[1:]:

                # 两种情况下，无法继续构成公共前缀：
                # 1. 当前字符串长度不够，没有第 i 个字符
                # 2. 当前字符串第 i 个字符与第一个字符串不同
                if i >= len(s) or s[i] != strs[0][i]:
                    return res

            # 所有字符串在位置 i 的字符都相同
            # 才能将这个字符加入公共前缀
            res += strs[0][i]

        return res