#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []

        for interval in sorted(intervals, key=lambda i: i[0]):
            if out and interval[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1], interval[-1])
            else:
                out.append(interval)

        return out
# @lc code=end

# Accepted
# 169/169 cases passed(92 ms)
# Your runtime beats 98.22 % of python3 submissions
# Your memory usage beats 6.52 % of python3 submissions(15.6 MB)
