#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        level = [root]

        while root and level:
            res += level[-1].val,
            level = [child for node in level for child in (
                node.left, node.right) if child]

        return res
# @lc code=end

# Accepted
# 211/211 cases passed(32 ms)
# Your runtime beats 90.65 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
