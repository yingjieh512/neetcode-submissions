import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))

        heap = []
        i = 0
        n = len(projects)

        for _ in range(k):

            # 找到所有目前可以启动的项目
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1

            # 没有项目可以做
            if not heap:
                break

            # 选择利润最高的项目
            w += -heapq.heappop(heap)

        return w