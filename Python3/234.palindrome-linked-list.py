#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1

        return True
# @lc code=end

# Accepted
# 26/26 cases passed(72 ms)
# Your runtime beats 90.45 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(22.8 MB)
