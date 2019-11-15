#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start


class Solution:
    def titleToNumber(self, s: str) -> int:
        number = 0
        for c in s:
            number = number*26 + ord(c) - ord('A') + 1

        return number
# @lc code=end

# Accepted
# 1000/1000 cases passed(28 ms)
# Your runtime beats 97.3 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
