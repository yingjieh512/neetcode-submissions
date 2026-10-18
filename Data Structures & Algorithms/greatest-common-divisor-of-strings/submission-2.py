
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 如果两个字符串不能由同一个基本字符串重复组成
        # 那么它们就不存在公共的字符串因子
        if str1 + str2 != str2 + str1:
            return ""

        # 求两个字符串长度的最大公约数
        length = gcd(len(str1), len(str2))

        # 返回前 length 个字符
        return str1[:length]
