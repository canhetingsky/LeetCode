#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for _ in range(n):
            p = p.next
        if not p:
            return head.next
        while p.next:
            p = p.next
            q = q.next
        delete = q.next
        q.next = delete.next

        return head
# @lc code=end
