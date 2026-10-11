class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        firstRow = False
        firstCol = False

        # 第一行原本是否有 0
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True

        # 第一列原本是否有 0
        for i in range(m):
            if matrix[i][0] == 0:
                firstCol = True

        # 使用第一行、第一列记录标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 根据标记清零内部元素
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最后处理第一行
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        # 最后处理第一列
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0