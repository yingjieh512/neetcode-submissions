class Solution:
    def jump(self, nums: List[int]) -> int:
        maxReach = 0
        currentEnd = 0
        steps = 0

        for i in range(len(nums) - 1):
            maxReach = max(maxReach, i + nums[i])

            if i == currentEnd:
                steps += 1
                currentEnd = maxReach

        return steps