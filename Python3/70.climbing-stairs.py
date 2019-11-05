#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        step = [0 for i in range(n)]
        step[0], step[1] = 1, 2
        for i in range(2, n):
            step[i] = step[i - 1] + step[i - 2]

        return step[-1]
# @lc code=end

# Accepted
# 45/45 cases passed(48 ms)
# Your runtime beats 5.81 % of python3 submissions
# Your memory usage beats 5.97 % of python3 submissions(13.9 MB)
