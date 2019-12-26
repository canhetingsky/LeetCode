#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        sum_val = 0
        left_level = [root.left] if root.left else []
        right_level = [root.right] if root.right else []

        while left_level or right_level:
            next_left_level, next_right_level = [], []

            for node in left_level:
                if not node.left and not node.right:  # find left leaves
                    sum_val += node.val
                if node.left:
                    next_left_level.append(node.left)
                if node.right:
                    next_right_level.append(node.right)

            for node in right_level:
                if node.left:
                    next_left_level.append(node.left)
                if node.right:
                    next_right_level.append(node.right)

            left_level = next_left_level
            right_level = next_right_level

        return sum_val
# @lc code=end

# Accepted
# 102/102 cases passed(28 ms)
# Your runtime beats 91.92 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.9 MB)
