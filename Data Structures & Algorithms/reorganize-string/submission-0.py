import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 负次数实现最大堆：剩余最多的字符优先
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(heap)

        res = []

        # 暂时扣住上一次使用的字符及其剩余次数
        prev_count = 0
        prev_char = ""

        while heap:
            count, char = heapq.heappop(heap)
            res.append(char)

            # 已经选好了不同字符，上一次的字符可以放回了
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # count 是负数，使用一次就加 1
            count += 1

            # 当前字符暂时不放回，避免下一次连续选到
            prev_count = count
            prev_char = char

        # 堆空了，但扣住的字符还有剩余，说明无法隔开
        if prev_count < 0:
            return ""

        return "".join(res)