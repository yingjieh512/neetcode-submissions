class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    if obstacleGrid[i+1][j]!=1:
                        dp[i+1][j]+=dp[i][j]

                if j + 1 < n:
                    if obstacleGrid[i][j+1]!=1:
                        dp[i][j+1]+=dp[i][j]

        return dp[m-1][n-1]