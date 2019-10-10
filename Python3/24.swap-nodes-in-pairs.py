#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = dummyHead = ListNode(0)
        curr.next = head
        while curr.next and curr.next.next:
            l = curr.next
            r = l.next

            curr.next, r.next, l.next = r, l, r.next

            curr = l

        return dummyHead.next
# @lc code=end
