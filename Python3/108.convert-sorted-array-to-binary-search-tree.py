#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        # The idea is to find the root first,
        # then recursively build each left and right subtree
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
# @lc code=end

# Accepted
# 32/32 cases passed(72 ms)
# Your runtime beats 87.97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.9 MB)
