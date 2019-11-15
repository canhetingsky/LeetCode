#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return min(self.stack)
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

# Accepted
# 18/18 cases passed(824 ms)
# Your runtime beats 18.25 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(16.1 MB)
