#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)
        for i in range(dim - 1):
            for j in range(i + 1, dim):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # swap

        for m in matrix:
            m.reverse()
# @lc code=end

# Accepted
# 21/21 cases passed(36 ms)
# Your runtime beats 96.66 % of python3 submissions
# Your memory usage beats 6.25 % of python3 submissions(13.8 MB)
