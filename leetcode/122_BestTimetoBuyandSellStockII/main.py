class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 0:
            return profit
        price_buy = prices[0]
        for idx in range(1, len(prices)):
            if prices[idx] < price_buy:
                price_buy = prices[idx]
            elif prices[idx] > price_buy:
                profit += prices[idx] - price_buy
                price_buy = prices[idx]

        return profit
