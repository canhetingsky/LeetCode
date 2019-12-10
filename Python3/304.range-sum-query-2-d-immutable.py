#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = []
        for i in range(len(matrix)):
            self.sums.append([0] * len(matrix[0]))
            for j in range(len(matrix[0])):
                if j == 0:
                    self.sums[i][j] = matrix[i][j]
                else:
                    self.sums[i][j] = self.sums[i][j - 1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                res += self.sums[i][col2]
            else:
                res += self.sums[i][col2] - self.sums[i][col1 - 1]

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

# Accepted
# 12/12 cases passed(232 ms)
# Your runtime beats 24.81 % of python3 submissions
# Your memory usage beats 83.33 % of python3 submissions(15.3 MB)
