class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=0
        p2=0
        res=[]
        while p1 < m or p2< n:
            if p1==m:
                for i in range(p2,n):
                    res.append(nums2[i])
                nums1[:] = res  # 原地修改 nums1
                return
            if p2==n:
                for j in range(p1,m):
                    res.append(nums1[j])
                nums1[:] = res  # 原地修改 nums1
                return
            if nums1[p1]<nums2[p2]:
                res.append(nums1[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
        nums1[:] = res  # 原地修改 nums1
        return
