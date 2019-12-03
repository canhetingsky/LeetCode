#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        res = []
        self.paths(root, res, [root.val])
        return res

    def paths(self, root: TreeNode, res: List[str], path: List[int]):
        if not root.left and not root.right:  # find leaf node
            res.append('->'.join(list(map(str, path))))
            return

        if root.left:
            self.paths(root.left, res, path + [root.left.val])2380348167
        if root.right:
            self.paths(root.right, res, path + [root.right.val])
# @lc code=end

# Accepted
# 209/209 cases passed(28 ms)
# Your runtime beats 94.77 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
