#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        has_odd = False
        res = 0
        for val in count.values():
            if val % 2 == 0:
                res += val
            elif has_odd:
                    res += (val - 1)
            else:
                res += val
                has_odd = True

        return res
# @lc code=end

# Accepted
# 95/95 cases passed (20 ms)
# Your runtime beats 99.72 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
