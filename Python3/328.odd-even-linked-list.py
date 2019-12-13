#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None

        odd.next = dummy2.next
        return dummy1.next
# @lc code=end

# Accepted
# 71/71 cases passed(44 ms)
# Your runtime beats 73.99 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.5 MB)
