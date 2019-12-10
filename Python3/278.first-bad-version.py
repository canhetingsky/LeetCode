#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = n - 1
        l = 0
        while(l <= r):
            mid = (l + r) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1

        return l
# @lc code=end

# Accepted
# 22/22 cases passed(28 ms)
# Your runtime beats 85.94 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
