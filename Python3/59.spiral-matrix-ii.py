#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)

        top, left, bottom, right = 0, 0, n - 1, n - 1
        num = 1
        while num <= n * n:
            for x in range(left, right + 1):
                matrix[top][x] = num
                num += 1
            top += 1

            for y in range(top, bottom + 1):
                matrix[y][right] = num
                num += 1
            right -= 1

            for x in range(right, left - 1, -1):
                matrix[bottom][x] = num
                num += 1
            bottom -= 1

            for y in range(bottom, top - 1, -1):
                matrix[y][left] = num
                num += 1
            left += 1

        return matrix
# @lc code=end

# Accepted
# 20/20 cases passed(36 ms)
# Your runtime beats 85.75 % of python3 submissions
# Your memory usage beats 9.09 % of python3 submissions(13.7 MB)
