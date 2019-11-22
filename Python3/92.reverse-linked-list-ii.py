#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:  # don't need to reverse
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for _ in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for _ in range(n - m + 1):
            next_node = cur.next
            cur.next = reverse
            reverse = cur
            cur = next_node

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next
# @lc code=end

# Accepted
# 44/44 cases passed(28 ms)
# Your runtime beats 98.44 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
