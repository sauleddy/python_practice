class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        profit = 0
        price_max = prices[-1]
        price_min = prices[-1]
        for price in prices[-2::-1]:
            if price > price_max:
                price_max = price
                price_min = price
            elif price < price_min:
                price_min = price
                if price_max - price_min > profit:
                    profit = price_max - price_min
        return profit


list_test = [1, 2, 3]
print(list_test[-1::-1])
