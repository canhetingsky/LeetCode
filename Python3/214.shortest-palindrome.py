#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]  # reverse
        for i in range(len(s) + 1):
            if s.startswith(rev[i:]):  # palindrome find
                return rev[:i] + s
# @lc code=end

# Accepted
# 120/120 cases passed(44 ms)
# Your runtime beats 94.42 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.2 MB)
