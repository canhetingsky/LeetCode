#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dump = ListNode(0)
        dump.next = head
        last_node = dump
        while head:
            if head.val == val:
                last_node.next = head.next
            else:
                last_node = head
            head = head.next

        return dump.next
# @lc code=end

# Accepted
# 65/65 cases passed(68 ms)
# Your runtime beats 93.97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(15.6 MB)
