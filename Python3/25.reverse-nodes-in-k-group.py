#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump = pre, l  # connect two k-groups
                l = r
            else:
                return dummy.next
# @lc code=end

# Accepted
# 81/81 cases passed(56 ms)
# Your runtime beats 65.71 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions(14.5 MB)
