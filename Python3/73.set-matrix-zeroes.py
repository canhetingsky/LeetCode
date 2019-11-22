#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in row:
                        row.append(i)
                    if j not in column:
                        column.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for j in column:
            for i in range(len(matrix)):
                matrix[i][j] = 0
# @lc code=end

# Accepted
# 159/159 cases passed(136 ms)
# Your runtime beats 99.87 % of python3 submissions
# Your memory usage beats 92.31 % of python3 submissions(13.4 MB)
