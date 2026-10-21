class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        def checksum(suming,nums,k):
            cur=0
            res=1
            for i in range(len(nums)):
                cur+=nums[i]
                if cur>suming:
                    cur=nums[i]
                    res+=1
            if res>k:
                return False
            else:
                return True
        while left<=right:
            mid=(left+right)//2
            if checksum(mid,nums,k):
                right=mid-1
            else:
                left=mid+1
        return left