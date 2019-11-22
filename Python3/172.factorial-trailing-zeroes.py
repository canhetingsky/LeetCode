#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start


class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res
# @lc code=end

# Accepted
# 502/502 cases passed(32 ms)
# Your runtime beats 88.85 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
