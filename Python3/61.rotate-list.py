#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        curr = head
        length = 0
        while curr:  # get the length of the input ListNode head
            length += 1
            curr = curr.next
        if length == 0:
            return None

        k = k % length  # get the real rotation k places
        if k == 0:  # no rotation required
            return head

        left = l = head
        for _ in range(length - k - 1):
            l = l.next
        right = r = l.next
        for _ in range(k - 1):
            r = r.next
        r.next = left
        l.next = None

        return right
# @lc code=end

# Accepted
# 231/231 cases passed(40 ms)
# Your runtime beats 86.85 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions(13.7 MB)
