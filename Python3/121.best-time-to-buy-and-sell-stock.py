#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need at least two prices
        # buy one and sell one share of the stock
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(prices[i] - min_price, max_profit)
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit
# @lc code=end

# Accepted
# 200/200 cases passed(64 ms)
# Your runtime beats 97.45 % of python3 submissions
# Your memory usage beats 94.25 % of python3 submissions(13.8 MB)
