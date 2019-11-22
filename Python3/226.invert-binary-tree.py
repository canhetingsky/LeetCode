#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        level = [root]
        while root and level:
            next_level = []
            for node in level:
                self.invertLeftAndRight(node)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level

        return root

    def invertLeftAndRight(self, node: TreeNode) -> None:
        node.left, node.right = node.right, node.left
# @lc code=end

# Accepted
# 68/68 cases passed(24 ms)
# Your runtime beats 98.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
