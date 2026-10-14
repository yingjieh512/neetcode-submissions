class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
            if count[nums[i]]>len(nums)/2:
                return nums[i]