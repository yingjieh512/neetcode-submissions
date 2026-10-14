class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)

        # 只需要遍历前一半
        for i in range(n // 2):

            # i 是左边元素的索引
            # n - 1 - i 是右边对称元素的索引
            # 交换两个位置的字符
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i]