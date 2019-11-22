#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows, columns = len(matrix), len(matrix[0])
        low, high = 0, rows * columns - 1

        # matrix are sorted
        while low <= high:
            mid = (low + high) // 2  # binary search
            num = matrix[mid // columns][mid % columns]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
# @lc code=end

# Accepted
# 136/136 cases passed(60 ms)
# Your runtime beats 99.94 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions(14.9 MB)
