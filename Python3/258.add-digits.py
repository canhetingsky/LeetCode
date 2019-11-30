#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:  # only one digit
            return num

        sum_val = 0
        for digit in str(num):
            sum_val += int(digit)

        return self.addDigits(sum_val)
# @lc code=end

# Accepted
# 1101/1101 cases passed(32 ms)
# Your runtime beats 84.28 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
