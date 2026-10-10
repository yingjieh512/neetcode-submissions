from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def bfs(q, visited):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):

                        visited.add((nr, nc))
                        q.append((nr, nc))

        pac_q = deque()
        atl_q = deque()

        # 上下边界
        for c in range(COLS):
            pac_q.append((0, c))
            pacific.add((0, c))

            atl_q.append((ROWS - 1, c))
            atlantic.add((ROWS - 1, c))

        # 左右边界
        for r in range(ROWS):
            pac_q.append((r, 0))
            pacific.add((r, 0))

            atl_q.append((r, COLS - 1))
            atlantic.add((r, COLS - 1))

        bfs(pac_q, pacific)
        bfs(atl_q, atlantic)

        return [[r, c] for r, c in pacific & atlantic]