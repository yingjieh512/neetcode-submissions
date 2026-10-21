class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=max(dp[i-j]*j,(i-j)*j,dp[i])
        return dp[n]