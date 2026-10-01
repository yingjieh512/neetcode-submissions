class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        have_seen=set()
        for i in range(len(nums)):
            if nums[i] not in have_seen:
                have_seen.add(nums[i])
            else:
                return True
        return False