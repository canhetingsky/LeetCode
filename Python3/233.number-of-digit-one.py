#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start


class Solution:
    def countDigitOne(self, n: int) -> int:
        nums = list(map(str, range(1, n + 1)))
        s = ''.join(nums)

        return s.count('1')
# @lc code=end

# Memory Limit Exceeded
# 36/40 cases passed(N/A)
# Testcase 824883294
