class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        len_prices = len(prices)
        if len_prices < 2:
            return 0
        dict_dp = {}
        return self.help(prices, len(prices)-1, dict_dp)

    def help(self, prices, idx_end, dict_dp):
        # print("end idx:", idx_end)
        while idx_end > 0:
            if prices[idx_end] > prices[idx_end - 1]:
                break
            idx_end -= 1
        if idx_end <= 0:
            return 0
        # print("end idx:", idx_end)

        profit_dp = dict_dp.get(idx_end, 0)
        if profit_dp > 0:
            return profit_dp
        max_price = prices[idx_end]
        idx = idx_end - 1
        max_profit = 0
        while prices[idx] <= max_price and idx >= 0:
            if prices[idx] < max_price:
                # print("profit:", idx, idx_end, max_price - prices[idx])
                profit_this = max_price - prices[idx] + self.help(prices, idx - 2, dict_dp)
                if profit_this > max_profit:
                    max_profit = profit_this
            idx -= 1
        if idx >= 0 and idx_end - idx == 2:
            profit_this = self.help(prices, idx, dict_dp)
            if profit_this > max_profit:
                max_profit = profit_this

        dict_dp[idx_end] = max_profit
        return max_profit

my_solution = Solution()
# print(my_solution.maxProfit([1, 2, 3, 1, 0, 2]))
print(my_solution.maxProfit([1, 7, 2, 4]))
