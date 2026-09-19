class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for price in prices:
            profit = max(prices[prices.index(price):]) - price
            if profit > max_profit:
                max_profit = profit

        return max_profit