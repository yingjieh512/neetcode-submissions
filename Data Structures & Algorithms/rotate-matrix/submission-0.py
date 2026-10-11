class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 第一步：转置
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第二步：反转每一行
        for i in range(n):
            left = 0
            right = n - 1

            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]

                left += 1
                right -= 1