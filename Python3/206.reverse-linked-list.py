#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre, cur = cur, next_node

        return pre
# @lc code=end

# Accepted
# 27/27 cases passed(28 ms)
# Your runtime beats 99.23 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.9 MB)
