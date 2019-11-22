#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        level_index = 0
        while root and level:
            node_value = []
            next_level = []
            for node in level:
                node_value.append(node.val)  # default:from left to right
                # find the next level of node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # handling special cases:right to left
            if level_index % 2 == 1:
                node_value.reverse()

            res.append(node_value)
            level = next_level
            level_index += 1

        return res
# @lc code=end

# Accepted
# 33/33 cases passed(24 ms)
# Your runtime beats 99.8 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
