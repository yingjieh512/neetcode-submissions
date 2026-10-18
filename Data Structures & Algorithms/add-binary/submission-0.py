
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # i 指向 a 的最后一个字符
        # j 指向 b 的最后一个字符
        # 因为加法要从最低位（最右边）开始
        i = len(a) - 1
        j = len(b) - 1

        # carry 记录进位
        # 例如 1 + 1 = 10，当前位写 0，向前进 1
        carry = 0

        # res 存储计算出来的每一位
        res = []

        # 只要 a 或 b 还有数字，或者还有进位，
        # 就需要继续计算
        while i >= 0 or j >= 0 or carry > 0:

            # total 先加上上一位传来的进位
            total = carry

            # 如果 a 还有数字，就加上 a 当前位
            if i >= 0:
                total += int(a[i])
                i -= 1

            # 如果 b 还有数字，就加上 b 当前位
            if j >= 0:
                total += int(b[j])
                j -= 1

            # 当前位应该写 total % 2
            #
            # 0 % 2 = 0
            # 1 % 2 = 1
            # 2 % 2 = 0
            # 3 % 2 = 1
            #
            # 因为从右往左计算，
            # 所以这里存进去的结果是反过来的
            res.append(str(total % 2))

            # 计算进位
            #
            # total = 0 或 1，carry = 0
            # total = 2 或 3，carry = 1
            carry = total // 2

        # res 是反过来的，因此需要翻转
        # join 把列表中的字符拼接成字符串
        return "".join(res[::-1])
