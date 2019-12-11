#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n//3)
# @lc code=end

# Accepted
# 21038/21038 cases passed(68 ms)
# Your runtime beats 94.71 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
