class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp = [[float("inf")] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(n):
                if i + 1 < m:
                    dp[i+1][j]=min(dp[i][j]+grid[i+1][j],dp[i+1][j])
                if j + 1 < n:
                    dp[i][j+1]=min(dp[i][j]+grid[i][j+1],dp[i][j+1])
        return dp[m-1][n-1]