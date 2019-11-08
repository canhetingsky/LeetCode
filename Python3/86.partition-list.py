#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        node1 = l = ListNode(0)
        node2 = r = ListNode(0)

        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        r.next = None
        l.next = node2.next  # link two lists

        return node1.next
# @lc code=end

# Accepted
# 166/166 cases passed(24 ms)
# Your runtime beats 99.95 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
