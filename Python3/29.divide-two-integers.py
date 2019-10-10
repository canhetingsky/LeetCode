#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1

        if not positive:
            result = -result
        return min(max(-2147483648, result), 2147483647)


# @lc code=end

# Accepted
# 989/989 cases passed(36 ms)
# Your runtime beats 88.2 % of python3 submissions
# Your memory usage beats 7.41 % of python3 submissions(13.9 MB)
