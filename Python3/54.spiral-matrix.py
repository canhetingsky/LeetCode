#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        xlen, ylen = len(matrix[0]), len(matrix)
        top, left, bottom, right = 0, 0, ylen - 1, xlen - 1
        result = []

        while True:
            for x in range(left, right + 1):
                result.append(matrix[top][x])
            top += 1
            if top > bottom:
                break

            for y in range(top, bottom + 1):
                result.append(matrix[y][right])
            right -= 1
            if left > right:
                break

            for x in range(right, left - 1, -1):
                result.append(matrix[bottom][x])
            bottom -= 1
            if top > bottom:
                break

            for y in range(bottom, top - 1, -1):
                result.append(matrix[y][left])
            left += 1
            if left > right:
                break

        return result
# @lc code=end

# Accepted
# 22/22 cases passed(32 ms)
# Your runtime beats 92.86 % of python3 submissions
# Your memory usage beats 8.7 % of python3 submissions(13.9 MB)
