#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)  # backtracking

        if n % 2:
            return x * self.myPow(x, n - 1)  # backtracking
        else:
            return self.myPow(x * x, n/2)  # binary-search

# @lc code=end

# Accepted
# 304/304 cases passed(36 ms)
# Your runtime beats 74.72 % of python3 submissions
# Your memory usage beats 6.9 % of python3 submissions(14.1 MB)
