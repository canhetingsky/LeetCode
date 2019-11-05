#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        try:
            float(s)
            return True
        except ValueError:
            return False
# @lc code=end

# Accepted
# 1481/1481 cases passed(36 ms)
# Your runtime beats 90.94 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions(14.1 MB)
