#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = [[1 for _ in range(n)] for _ in range(m)]
        # there is only one road at the edge
        for i in range(1, m):
            for j in range(1, n):
                # the robot can move either down or right
                steps[i][j] = steps[i-1][j] + steps[i][j-1]
        return steps[-1][-1]
# @lc code=end

# Accepted
# 62/62 cases passed(40 ms)
# Your runtime beats 45.51 % of python3 submissions
# Your memory usage beats 5.77 % of python3 submissions(13.8 MB)
