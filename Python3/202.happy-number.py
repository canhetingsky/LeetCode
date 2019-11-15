#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start


class Solution:
    def isHappy(self, n: int) -> bool:
        res = [n]
        while n != 1:
            n = self.getSum(n)
            if n in res:  # it will loop endlessly in a cycle, so return false
                return False
            else:
                res.append(n)

        return True

    def getSum(self, n: int) -> int:
        """
        the sum of the squares of its digits
        """
        sum_squares = 0
        while n > 0:
            sum_squares += pow(n % 10, 2)
            n //= 10
        return sum_squares
# @lc code=end

# Accepted
# 401/401 cases passed(32 ms)
# Your runtime beats 95.88 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
