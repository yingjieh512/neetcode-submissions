from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Python 默认是 Min Heap，用负数模拟 Max Heap
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        q = deque()  # (剩余次数, 可以重新执行的时间)
        time = 0

        while maxHeap or q:
            time += 1

            # 执行剩余次数最多的 Task
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                freq += 1  # 负数向 0 靠近，表示完成了一次

                if freq < 0:
                    q.append((freq, time + n))

            # 检查有没有 Task 结束 Cooldown
            if q and q[0][1] == time:
                freq, readyTime = q.popleft()
                heapq.heappush(maxHeap, freq)

        return time