class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=0
        profit=0
        for i in range(1,len(prices)):
            if prices[i]-prices[left]>profit:
                profit=prices[i]-prices[left]
            elif prices[i]<prices[left]:
                left=i

        return profit