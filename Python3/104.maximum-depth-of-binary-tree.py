#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth, level = 0, [root]
        while root and level:
            next_level = []
            for node in level:
                # find the next level of node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            depth += 1
            level = next_level

        return depth
# @lc code=end

# Accepted
# 39/39 cases passed(40 ms)
# Your runtime beats 97.25 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.8 MB)
