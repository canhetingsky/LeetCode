#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:  # binary search
            mid = (l + r) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                l = mid + 1
            else:
                r = mid-1
# @lc code=end

# Accepted
# 25/25 cases passed(24 ms)
# Your runtime beats 81.03 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
