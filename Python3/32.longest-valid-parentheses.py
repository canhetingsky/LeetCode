#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        left_count = right_count = 0
        for i in range(len(s)):  # left to right scan
            if s[i] == '(':
                left_count += 1
            elif s[i] == ')':
                right_count += 1

            if left_count == right_count:
                max_length = max(max_length, right_count * 2)
            elif left_count < right_count:
                left_count = right_count = 0

        left_count = right_count = 0
        for i in range(len(s))[::-1]:  # right to left scan
            if s[i] == '(':
                left_count += 1
            elif s[i] == ')':
                right_count += 1

            if left_count == right_count:
                max_length = max(max_length, left_count * 2)
            elif left_count > right_count:
                left_count = right_count = 0

        return max_length
# @lc code=end

# Accepted
# 230/230 cases passed(48 ms)
# Your runtime beats 90.94 % of python3 submissions
# Your memory usage beats 44.44 % of python3 submissions(13.8 MB)
