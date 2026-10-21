class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        res=[]
        def dfs(i,cur,numss):
            if len(cur) == k:
                res.append(cur.copy())
                return

            if i >= len(numss) :
                return
            cur.append(numss[i])
            dfs(i + 1, cur, numss)
            cur.pop()
            dfs(i + 1, cur, numss)

        dfs(0, [], nums)
        return res