#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[-1]
        left, right = [], []
        for interval in intervals:
            if interval[-1] < start:  # non-overlapping
                left += interval,
            elif interval[0] > end:  # non-overlapping
                right += interval,
            else:
                start = min(start, interval[0])
                end = max(end, interval[-1])

        return left + [[start, end]] + right
# @lc code=end

# Accepted
# 154/154 cases passed(88 ms)
# Your runtime beats 93.31 % of python3 submissions
# Your memory usage beats 8 % of python3 submissions(17.3 MB)
