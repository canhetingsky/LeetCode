#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        p = l1
        q = l2
        curr = dummyHead
        carry = 0

        while p or q:
            if p:
                val1 = p.val
            else:
                val1 = 0
            if q:
                val2 = q.val
            else:
                val2 = 0

            sum = carry + val1 + val2
            carry = sum // 10
            curr.next = ListNode(sum % 10)

            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummyHead.next
