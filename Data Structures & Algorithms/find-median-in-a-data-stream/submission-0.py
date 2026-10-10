import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max Heap (负数模拟)
        self.large = []  # Min Heap

    def addNum(self, num: int) -> None:
        # 先加入左半边
        heapq.heappush(self.small, -num)

        # 保证 small 所有数 <= large 所有数
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # 平衡两个 Heap 的大小
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2