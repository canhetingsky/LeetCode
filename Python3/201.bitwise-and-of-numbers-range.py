#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n = n & (n - 1)

        return n
# @lc code=end

# Accepted
# 8266/8266 cases passed(48 ms)
# Your runtime beats 98.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
