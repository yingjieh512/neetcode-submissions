class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        def canload(ship,weight,days):
            curship=0
            day=1#至少要一天，如果从未超重就是1
            for i in range(len(weight)):
                curship+=weight[i]
                if curship>ship:
                    day+=1
                    curship=weight[i]
            if day<=days:
                return True
            return False

        while left<=right:
            mid=(left+right)//2
            if canload(mid,weights,days):
                right=mid-1
            else:
                left=mid+1
        return left

            