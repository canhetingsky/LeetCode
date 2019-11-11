#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        pre = self.generate(numRows - 1)  # backtracking
        lastRow = pre[-1]
        cur = [1]
        for i in range(1, len(lastRow)):
            cur.append(lastRow[i] + lastRow[i - 1])
        cur.append(1)
        pre.append(cur)

        return pre
# @lc code=end

# Accepted
# 15/15 cases passed(28 ms)
# Your runtime beats 97.93 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
