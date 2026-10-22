import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        res = []

        while heap:
            count, char = heapq.heappop(heap)

            # 如果连续两个字符都等于当前字符
            if len(res) >= 2 and res[-1] == res[-2] == char:

                # 没有其他字符可以使用
                if not heap:
                    break

                # 取第二多的字符
                count2, char2 = heapq.heappop(heap)

                res.append(char2)
                count2 += 1

                if count2 < 0:
                    heapq.heappush(heap, (count2, char2))

                # 第一个字符还没使用，放回 heap
                heapq.heappush(heap, (count, char))

            else:
                res.append(char)
                count += 1

                if count < 0:
                    heapq.heappush(heap, (count, char))

        return "".join(res)