#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = 1
        while True:
            if res == n:
                return True
            elif res > n:
                return False
            res *= 2
# @lc code=end

# Accepted
# 1108/1108 cases passed(32 ms)
# Your runtime beats 84.78 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.9 MB)
