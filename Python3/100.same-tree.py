#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p and q are both None
        if not p and not q:
            return True

        # only one of p and q is None
        if not p or not q:
            return False

        # p and q are both not None
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

# Accepted
# 57/57 cases passed(28 ms)
# Your runtime beats 97.39 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
