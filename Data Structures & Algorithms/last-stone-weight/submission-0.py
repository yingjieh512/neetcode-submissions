class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # 最大
            x = -heapq.heappop(heap)  # 第二大

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0