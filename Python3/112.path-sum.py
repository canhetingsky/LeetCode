#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        # a leaf is a node with no children
        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
# @lc code=end

# Accepted
# 114/114 cases passed(40 ms)
# Your runtime beats 98.33 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.6 MB)
