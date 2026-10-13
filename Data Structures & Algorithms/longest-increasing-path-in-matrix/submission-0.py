
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # dp[r][c] 表示：
        # 以 (r, c) 为终点的最长递增路径长度
        # 每个格子自己就构成长度为 1 的路径
        dp = [[1] * cols for _ in range(rows)]

        # 收集所有格子的数值和坐标
        cells = []

        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))

        # 按照数值从小到大排序
        # 这样计算当前格子时，
        # 所有比它小的格子都已经计算完成
        cells.sort()

        # 上、下、左、右
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        result = 1

        # 从数值最小的格子开始计算
        for value, r, c in cells:

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 检查邻居是否在矩阵内
                if 0 <= nr < rows and 0 <= nc < cols:

                    # 只能从更小的邻居走到当前格子
                    if matrix[nr][nc] < value:

                        # 当前格子接在邻居的最长路径后面
                        dp[r][c] = max(
                            dp[r][c],
                            dp[nr][nc] + 1
                        )

            # 更新整个矩阵的最长路径长度
            result = max(result, dp[r][c])

        return result
