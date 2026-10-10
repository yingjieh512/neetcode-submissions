from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # 把所有 treasure chest 加入 queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 2147483647):

                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))