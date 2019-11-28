#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if left_depth == right_depth:
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            return pow(2, right_depth) + self.countNodes(root.left)

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
# @lc code=end

# Accepted
# 18/18 cases passed(76 ms)
# Your runtime beats 95.44 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(19.9 MB)
