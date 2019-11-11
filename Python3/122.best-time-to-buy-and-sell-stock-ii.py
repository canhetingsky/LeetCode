#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need at least two prices
        # buy one and sell one share of the stock
        if len(prices) < 2:
            return 0

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  # greedy
                profit += prices[i] - prices[i-1]

        return profit
# @lc code=end

# Accepted
# 201/201 cases passed(64 ms)
# Your runtime beats 95.42 % of python3 submissions
# Your memory usage beats 73.17 % of python3 submissions(13.9 MB)
