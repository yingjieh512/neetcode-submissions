class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist.copy()

            for a, b, price in flights:
                if dist[a] + price < temp[b]:
                    temp[b] = dist[a] + price

            dist = temp

        if dist[dst] == float('inf'):
            return -1

        return dist[dst]
        ##bellman ford