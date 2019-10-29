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
        right_str = s.count(')')
        for i in range(len(s)):
            if i + max_length > len(s):
                break
            left_count = right_count = 0
            count, j = 0, i
            while j < len(s):
                if s[j] == '(':
                    left_count += 1
                elif s[j] == ')':
                    right_count += 1

                if left_count == right_count:
                    count = left_count * 2
                elif left_count < right_count:
                    break

                if (left_count - right_count) > (len(s) - j):
                    break
                if left_count > right_str:
                    break
                j += 1
            max_length = max(max_length, count)

        return max_length
# @lc code=end

# Time Limit Exceeded
# 228/230 cases passed(N/A)
