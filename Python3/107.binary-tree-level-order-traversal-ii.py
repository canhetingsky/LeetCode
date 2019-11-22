#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]

        while root and level:
            values = []
            next_level = []
            for node in level:
                values.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            res.append(values)
            level = next_level

        res.reverse()  # bottom-up
        return res
# @lc code=end

# Accepted
# 34/34 cases passed(36 ms)
# Your runtime beats 93.04 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13 MB)
