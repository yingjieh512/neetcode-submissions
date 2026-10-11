class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minDist = [float('inf')] * n
        minDist[0] = 0
        res = 0

        for _ in range(n):
            curr = -1

            for i in range(n):
                if i not in visited:
                    if curr == -1 or minDist[i] < minDist[curr]:
                        curr = i

            visited.add(curr)
            res += minDist[curr]

            for i in range(n):
                if i not in visited:
                    dist = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                    minDist[i] = min(minDist[i], dist)

        return res