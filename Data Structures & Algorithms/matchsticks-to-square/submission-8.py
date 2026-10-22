class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length=sum(matchsticks)//4
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        if matchsticks[0] > length:
            return False
        matchsticks.sort(reverse=True)
        sides=[0,0,0,0]
        def dfs(i,sides,matchsticks):
            if i==len(matchsticks):
                return True
            for j in range(len(sides)):
                if sides[j]+matchsticks[i]>length:
                    continue
                else:
                    sides[j]+=matchsticks[i]
                    if dfs(i+1,sides,matchsticks):
                        return True
                    sides[j]-=matchsticks[i]
                    # 空边都一样，放这条空边失败，就不用尝试其他空边
            return False

        dfs(0,sides,matchsticks)
        for num in sides:
            if num!=length:
                return False
        return True
            
