#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        last_parenthesis = self.generateParenthesis(n - 1)
        stack = []
        for parenthesis in last_parenthesis:
            for i in range(len(parenthesis)):
                if parenthesis[i] == ')':
                    new_str = self.insertString(parenthesis, i, ')(')
                    if not new_str in stack:
                        stack.append(new_str)
                    new_str = self.insertString(parenthesis, i, '()')
                    if new_str not in stack:
                        stack.append(new_str)
                    new_str = self.insertString(parenthesis, i + 1, '()')
                    if new_str not in stack:
                        stack.append(new_str)

        return stack

    def insertString(self, s: str, index: int, c: str) -> str:
        if index >= len(s):
            return s + c
        return s[:index] + c + s[index:]
# @lc code=end
