#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start


class Solution:
    def integerReplacement(self, n: int, counter=0) -> int:
        if n == 1:
            return counter
        if not n % 2:
            return self.integerReplacement(n/2, counter+1)
        else:
            return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))
# @lc code=end

# Accepted
# 47/47 cases passed(312 ms)
# Your runtime beats 15.94 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
