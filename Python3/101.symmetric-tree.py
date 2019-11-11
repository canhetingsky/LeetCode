#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)
# @lc code=end

# Accepted
# 195/195 cases passed(36 ms)
# Your runtime beats 91.06 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
