#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return

        # O(n*n/2) space, top-down
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:  # left side
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:  # right side
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                else:
                    res[i][j] = min(res[i - 1][j - 1],
                                    res[i - 1][j]) + triangle[i][j]

        return min(res[-1])


# @lc code=end

# Accepted
# 43/43 cases passed(64 ms)
# Your runtime beats 93.67 % of python3 submissions
# Your memory usage beats 20 % of python3 submissions(13.8 MB)
