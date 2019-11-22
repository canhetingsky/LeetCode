#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack:
            return self.stack.pop(0)  # FIFO
        return None

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack:
            return self.stack[0]  # FIFO
        return None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

# Accepted
# 17/17 cases passed(24 ms)
# Your runtime beats 97.49 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
