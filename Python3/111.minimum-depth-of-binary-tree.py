#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        level = [root]
        level_index = 0
        while root and level:
            level_index += 1
            next_level = []
            for node in level:
                if not node.left and not node.right:
                    return level_index  # a leaf is a node with no children.
                # find the next level of node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level

        return level_index
# @lc code=end

# Accepted
# 41/41 cases passed(36 ms)
# Your runtime beats 99.56 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.8 MB)
