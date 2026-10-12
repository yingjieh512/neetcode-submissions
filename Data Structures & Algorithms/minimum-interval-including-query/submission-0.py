import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        res = {}
        i = 0

        for q in sorted(queries):

            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            res[q] = heap[0][0] if heap else -1

        return [res[q] for q in queries]