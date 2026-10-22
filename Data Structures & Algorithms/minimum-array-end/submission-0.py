class Solution:
    def minEnd(self, n: int, x: int) -> int:
        remaining = n - 1
        answer = x
        bit = 1

        while remaining:
            # x 的这一位是 0，才能填入一个二进制位
            if (x & bit) == 0:
                if remaining & 1:
                    answer |= bit

                remaining >>= 1

            # 继续检查 x 的下一位
            bit <<= 1

        return answer