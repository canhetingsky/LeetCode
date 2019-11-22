#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]
# @lc code=end

# Accepted
# 61/61 cases passed(112 ms)
# Your runtime beats 79.9 % of python3 submissions
# Your memory usage beats 19.3 % of python3 submissions(15.4 MB)
