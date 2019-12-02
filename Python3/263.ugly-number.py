#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start


class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:  # Ugly numbers are positive numbers
            return False
        # prime factors only include 2, 3, 5
        # 1 is typically treated as an ugly number
        if num in [1, 2, 3, 5]:
            return True

        if num % 2 == 0:
            return self.isUgly(num // 2)
        if num % 3 == 0:
            return self.isUgly(num // 3)
        if num % 5 == 0:
            return self.isUgly(num // 5)

        return False
# @lc code=end

# Accepted
# 1012/1012 cases passed(28 ms)
# Your runtime beats 94.16 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
