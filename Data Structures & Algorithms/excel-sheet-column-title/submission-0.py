class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = ""

        while columnNumber > 0:

            # 因为 Excel 是从 1 开始的
            # 所以先减去 1，转换成从 0 开始
            columnNumber -= 1

            # 取当前最低位，对应 0~25
            remainder = columnNumber % 26

            # chr(65) = 'A'
            # chr(66) = 'B'
            # ...
            # chr(90) = 'Z'
            char = chr(65 + remainder)

            # 新字符放在前面
            res = char + res

            # 去掉已经处理的最低位
            columnNumber = columnNumber // 26

        return res