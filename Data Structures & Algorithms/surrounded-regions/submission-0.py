class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        def dfs(r, c):
            # 越界或者不是 O，直接返回
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != "O":
                return

            # 标记为 T，表示这个 O 不能被翻转
            board[r][c] = "T"

            # 搜索上下左右
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 从第一行和最后一行开始 DFS
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        # 从第一列和最后一列开始 DFS
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)

        # 遍历整个 board
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"  # 被包围，翻转
                elif board[r][c] == "T":
                    board[r][c] = "O"  # 没被包围，恢复