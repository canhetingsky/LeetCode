#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for ch in s:
            if ch in mapping:
                last = stack.pop() if stack else ''
                if mapping[ch] != last:
                    return False
            else:
                stack.append(ch)
        return not stack
# @lc code=end
