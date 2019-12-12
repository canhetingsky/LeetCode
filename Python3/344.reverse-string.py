#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1  # two pointers
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
# @lc code=end

# Accepted
# 478/478 cases passed(200 ms)
# Your runtime beats 99.32 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(17.1 MB)
