#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        while root and level:
            node_value = []
            next_level = []
            for node in level:
                node_value.append(node.val)
                # find the next level of node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            res.append(node_value)
            level = next_level

        return res
# @lc code=end

# Accepted
# 34/34 cases passed(44 ms)
# Your runtime beats 51.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13 MB)
