class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        res=[]
        res_set=set()
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
            if count[nums[i]]>len(nums)/3 and nums[i] not in res_set:
                res.append(nums[i])
                res_set.add(nums[i])
        return res

