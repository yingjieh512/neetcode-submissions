
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        # 记录每个字符最后一次出现的位置
        last = {}

        for i, c in enumerate(s):
            last[c] = i

        # 当前区间的起点
        start = 0

        # 当前区间需要延伸到的最远位置
        end = 0

        # 存储每个分割区间的长度
        result = []

        # 从左到右遍历字符串
        for i, c in enumerate(s):

            # 当前字符可能在后面再次出现
            # 因此更新当前区间的最远边界
            end = max(end, last[c])#必须覆盖所有遇到的字母的最远出现的地方

            # 如果当前下标已经到达区间最远边界
            # 说明区间内所有字符都不会在后面再次出现
            if i == end:

                # 计算当前区间长度
                result.append(end - start + 1)

                # 下一个区间从当前位置的下一位开始
                start = i + 1

        return result
