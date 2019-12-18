#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.nums)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

# Accepted
# 7/7 cases passed(68 ms)
# Your runtime beats 99.29 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(15.8 MB)
