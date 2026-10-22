class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length=sum(nums)//k
        total = sum(nums)
        nums.sort(reverse=True)
        if total % k != 0:
            return False
        if nums[0] > length:
            return False
        sides=[0]*k
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
                    if sides[j] == 0:
                        break
            return False

        return dfs(0,sides,nums)