class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]=max(dp[i-j]*j,(i-j)*j,dp[i])#是不保留“我这个数单独拿出来给别人”的情况的，因为一定要拆成两半或以上，所以dp[i]不记录i自己成为别人一部分的情况
        return dp[n]