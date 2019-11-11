#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        pre = self.getRow(rowIndex - 1)  # backtracking
        cur = [1]
        for i in range(1, len(pre)):
            cur.append(pre[i] + pre[i - 1])
        cur.append(1)

        return cur
# @lc code=end

# Accepted
# 34/34 cases passed(24 ms)
# Your runtime beats 99.62 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
