import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        # 添加原始 index
        tasks = [(start, duration, i)
                 for i, (start, duration) in enumerate(tasks)]

        # 按照任务到达时间排序
        tasks.sort()

        heap = []
        time = 0
        i = 0
        res = []

        while i < n or heap:

            # CPU 空闲，没有可执行任务
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # 将所有已经到达的任务加入 heap
            while i < n and tasks[i][0] <= time:
                start, duration, idx = tasks[i]
                heapq.heappush(heap, (duration, idx))
                i += 1

            # 选出处理时间最短的任务
            duration, idx = heapq.heappop(heap)

            res.append(idx)
            time += duration

        return res