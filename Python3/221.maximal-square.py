#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j]:
                    matrix[i][j] = min(matrix[i - 1][j - 1],
                                       matrix[i - 1][j], matrix[i][j - 1]) + 1

        return len(matrix) and max(map(max, matrix)) ** 2
# @lc code=end

# Accepted
# 68/68 cases passed(216 ms)
# Your runtime beats 57.95 % of python3 submissions
# Your memory usage beats 95.45 % of python3 submissions(13.8 MB)
