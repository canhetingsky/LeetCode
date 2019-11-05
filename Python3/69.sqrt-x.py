#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1
# @lc code=end

# Accepted
# 1017/1017 cases passed(44 ms)
# Your runtime beats 59.99 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions(13.9 MB)
