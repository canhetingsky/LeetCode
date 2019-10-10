#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        curr = dummyHead = ListNode(0)
        while p and q:
            if p.val < q.val:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next

        curr.next = p or q
        return dummyHead.next
# @lc code=end
