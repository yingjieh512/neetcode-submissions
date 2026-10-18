
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # 第一步：判断两个字符串是否有共同的重复模式
        #
        # 假设存在一个公共字符串 x，使得：
        # str1 = x 重复 m 次
        # str2 = x 重复 n 次
        #
        # 那么：
        # str1 + str2 = x 重复 (m+n) 次
        # str2 + str1 = x 重复 (n+m) 次
        #
        # 因为 m+n == n+m，所以两种拼接结果一定相等
        #
        # 例如：
        # str1 = "ABAB", str2 = "AB"
        # str1 + str2 = "ABABAB"
        # str2 + str1 = "ABABAB"
        #
        # 如果两种拼接结果不相等，
        # 就说明不可能存在一个字符串 x，
        # 通过重复 x 同时组成 str1 和 str2
        # 因此直接返回空字符串
        if str1 + str2 != str2 + str1:
            return ""

        # 第二步：计算两个字符串长度的最大公约数
        #
        # 如果 x 是公共字符串因子，
        # 那么 x 的长度必须同时整除 str1 和 str2 的长度
        #
        # 例如：
        # str1 = "NANANA"，长度为 6
        # str2 = "NANA"，长度为 4
        #
        # gcd(6, 4) = 2
        # 说明最长公共重复单元的长度为 2
        length = gcd(len(str1), len(str2))

        # 第三步：截取 str1 的前 length 个字符
        #
        # 例如：
        # str1 = "NANANA"
        # length = 2
        # str1[:2] = "NA"
        #
        # "NA" 重复 3 次得到 "NANANA"
        # "NA" 重复 2 次得到 "NANA"
        #
        # 因此 "NA" 就是最大的公共字符串因子
        return str1[:length]
