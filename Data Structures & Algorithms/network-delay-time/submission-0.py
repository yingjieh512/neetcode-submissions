class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        import heapq

        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        minHeap = [(0, k)]

        while minHeap:
            time, node = heapq.heappop(minHeap)

            # 这个是旧的、更差的距离
            if time > dist[node]:
                continue

            for nei, weight in graph[node]:
                new_time = time + weight

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(minHeap, (new_time, nei))

        answer = max(dist[1:])

        return answer if answer != float("inf") else -1