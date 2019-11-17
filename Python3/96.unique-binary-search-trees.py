#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                res[i] += res[j] * res[i - j - 1]

        return res[n]
# @lc code=end

# Accepted
# 19/19 cases passed(40 ms)
# Your runtime beats 27.84 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
