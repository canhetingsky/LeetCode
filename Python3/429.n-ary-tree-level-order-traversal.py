#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        level = [root]

        while root and level:
            level_val = []
            next_level = []
            for node in level:
                level_val.append(node.val)
                for child in node.children:
                    next_level.append(child)
            level = next_level
            res.append(level_val)

        return res
# @lc code=end

# Accepted
# 37/37 cases passed(44 ms)
# Your runtime beats 98.91 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.6 MB)
