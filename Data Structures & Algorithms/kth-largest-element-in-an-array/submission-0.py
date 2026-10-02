import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]

        heapq.heapify(heap)

        for _ in range(k):
            ans = -heapq.heappop(heap)

        return ans