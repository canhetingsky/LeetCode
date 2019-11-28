#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        total = (A - C) * (B - D) + (E - G) * (F - H)
        return total - overlap
# @lc code=end

# Accepted
# 3082/3082 cases passed(56 ms)
# Your runtime beats 81.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
