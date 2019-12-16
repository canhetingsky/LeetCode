#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2  # binary search
            if mid * mid == num:
                return True
            elif mid * mid < num:
                l = mid + 1
            else:
                r = mid - 1

        return False
# @lc code=end

# Accepted
# 68/68 cases passed(24 ms)
# Your runtime beats 95.53 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
