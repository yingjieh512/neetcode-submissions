class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m = len(matrix)
        n = len(matrix[0])

        # 不额外添加一圈 0
        self.prefix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                # 当前元素
                current = matrix[i][j]

                # 上面的矩形和
                top = 0
                if i > 0:
                    top = self.prefix[i - 1][j]

                # 左边的矩形和
                left = 0
                if j > 0:
                    left = self.prefix[i][j - 1]

                # 左上角重复的部分
                overlap = 0
                if i > 0 and j > 0:
                    overlap = self.prefix[i - 1][j - 1]

                # 计算当前前缀和
                self.prefix[i][j] = current + top + left - overlap

    def sumRegion(self, row1: int, col1: int,
                  row2: int, col2: int) -> int:

        # 整个大矩形
        total = self.prefix[row2][col2]

        # 减去上面的区域
        top = 0
        if row1 > 0:
            top = self.prefix[row1 - 1][col2]

        # 减去左边的区域
        left = 0
        if col1 > 0:
            left = self.prefix[row2][col1 - 1]

        # 加回左上角重复减去的区域
        overlap = 0
        if row1 > 0 and col1 > 0:
            overlap = self.prefix[row1 - 1][col1 - 1]

        return total - top - left + overlap