#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)  # m x n grid

        # there is only one or zero road at the edge
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(n):
            if i == 0:  # first row
                for j in range(1, m):
                    if obstacleGrid[i][j] == 0 and obstacleGrid[i][j-1] == 1:
                        obstacleGrid[i][j] = 1
                    else:  # obstacle
                        obstacleGrid[i][j] = 0
            else:  # first column
                if obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1:
                    obstacleGrid[i][0] = 1
                else:  # obstacle
                    obstacleGrid[i][0] = 0

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j]:  # obstacle
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + \
                        obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1]
# @lc code=end

# Accep
# 43/43 cases passed(56 ms)
# Your runtime beats 61.11 % of python3 submissions
# Your memory usage beats 8.89 % of python3 submissions(13.9 MB)
