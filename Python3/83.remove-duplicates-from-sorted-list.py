#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dump = pre = ListNode(0)
        dump.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dump.next
# @lc code=end

# Accepted
# 165/165 cases passed(40 ms)
# Your runtime beats 97.87 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
