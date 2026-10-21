class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n=len(nums)
        # dp=[0]*n#到i为止的possible way?
        # for i in range(nums):
        #     for j in range(i):
        #         dp[target-nums[j]]
        dp=[0]*(target+1)#dp[s]：用 nums 中的数字凑出总和 s，有多少种有顺序的方案。
        dp[0]=1
        for s in range(1, target + 1):  # 当前要凑出的总和
            for num in nums:
                if s>=num:
                   dp[s]+=dp[s-num]
        return dp[target]
