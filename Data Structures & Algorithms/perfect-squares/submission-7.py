class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1]=1#在i处最少能几个完全平方加起来
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        for num in range(2,n+1):
            for sq in squares:
                if num >= sq:
                   dp[num]=min(dp[num-sq]+1,dp[num])
        return dp[n]

