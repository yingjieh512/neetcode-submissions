class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # m 是原矩阵的行数
        m = len(matrix)

        # n 是原矩阵的列数
        n = len(matrix[0])

        # 创建新矩阵，注意行列需要交换
        # 原来 m 行 n 列，现在 n 行 m 列
        new_mat = [[0] * m for i in range(n)]

        # 遍历原矩阵每一个元素
        for i in range(m):
            for j in range(n):

                # 原来的 [i][j] 变成 [j][i]
                new_mat[j][i] = matrix[i][j]

        return new_mat