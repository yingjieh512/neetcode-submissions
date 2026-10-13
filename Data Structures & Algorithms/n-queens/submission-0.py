class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []   # 所有合法棋盘
        board = [["."] * n for _ in range(n)]

        cols = set()       # 已经被占用的列
        posDiag = set()    # 已占用的 row + col 对角线
        negDiag = set()    # 已占用的 row - col 对角线

        # row 表示当前准备在哪一行放 Queen
        def dfs(row):

            # Base case：所有 n 行都放好了 Queen
            if row == n:
                # 把每一行转成字符串
                res.append(["".join(r) for r in board])
                return

            # 尝试当前行的每一列
            for col in range(n):

                # 判断当前格子是否受到攻击
                if (col in cols or
                    row + col in posDiag or
                    row - col in negDiag):
                    continue

                # 1. 放置 Queen
                board[row][col] = "Q"

                # 标记列和对角线被占用
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                # 2. DFS：继续放下一行的 Queen
                dfs(row + 1)

                # 3. Backtracking：撤销刚才的 Queen
                board[row][col] = "."

                # 恢复列和对角线的可用状态
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        dfs(0)
        return res