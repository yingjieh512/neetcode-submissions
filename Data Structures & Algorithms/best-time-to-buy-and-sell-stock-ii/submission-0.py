class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 记录目前获得的总利润
        profit = 0

        # 从第二天开始遍历股票价格
        for i in range(1, len(prices)):

            # 如果今天的价格比昨天高
            # 说明这段上涨可以产生利润
            if prices[i] > prices[i - 1]:

                # 把今天和昨天的差价加入总利润
                profit += prices[i] - prices[i - 1]

        # 返回最大总利润
        return profit