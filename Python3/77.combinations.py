#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[i for i in range(1, n + 1)]]
        if k == 1:
            return [[i] for i in range(1, n + 1)]

        return [pre+[n]for pre in self.combine(n - 1, k - 1)] + self.combine(n - 1, k)
# @lc code=end

# Accepted
# 27/27 cases passed(88 ms)
# Your runtime beats 99.11 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.4 MB)
