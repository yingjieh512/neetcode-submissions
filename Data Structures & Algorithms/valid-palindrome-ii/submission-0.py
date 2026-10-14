class Solution:
    def validPalindrome(self, s: str) -> bool:

        # 检查 s[left:right+1] 是否是回文
        def check(left, right):

            while left < right:

                # 如果左右字符不同，说明不是回文
                if s[left] != s[right]:
                    return False

                # 左右指针向中间移动
                left += 1
                right -= 1

            # 所有字符都匹配，说明是回文
            return True

        left = 0
        right = len(s) - 1

        while left < right:

            # 如果左右字符相同，继续向中间走
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                # 左右字符不同，必须删除一个字符
                # 情况 1：跳过左边字符
                # 情况 2：跳过右边字符
                # 只要有一种情况是回文，就返回 True
                return check(left + 1, right) or check(left, right - 1)

        # 如果从头到尾都没有冲突，本身就是回文
        return True