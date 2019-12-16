#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n > 10 or n == 0:
            return 1  # only 0
        digits = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        res = 1  # 0
        fac = 1
        for i in range(n):
            fac *= digits[i]
            res += fac
        return res
# @lc code=end

# Accepted
# 9/9 cases passed(24 ms)
# Your runtime beats 94.52 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
