class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        visited = set()
        res = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i, j = 0, 0
        d = 0

        while True:
            res.append(matrix[i][j])
            visited.add((i, j))

            if len(res) == m * n:
                break

            di, dj = directions[d]
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in visited:
                d = (d + 1) % 4
                di, dj = directions[d]
                ni, nj = i + di, j + dj

            i, j = ni, nj

        return res