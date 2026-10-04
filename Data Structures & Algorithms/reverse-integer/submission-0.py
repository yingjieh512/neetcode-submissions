class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        res = 0

        while x != 0:
            if x > 0:
                digit = x % 10
            else:
                digit = x % -10

            # 去掉最后一位
            x = (x - digit) // 10

            # 正数溢出检查
            if res > 214748364 or (
                res == 214748364 and digit > 7
            ):
                return 0

            # 负数溢出检查
            if res < -214748364 or (
                res == -214748364 and digit < -8
            ):
                return 0

            res = res * 10 + digit

        return res