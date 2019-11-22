#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            oneDigitNum = int(s[i-1])
            twoDigitNum = int(s[i-2:i])

            # dynamic programming
            if oneDigitNum > 0:
                dp[i] = dp[i-1]
            if 10 <= twoDigitNum <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]
# @lc code=end

# Accepted
# 258/258 cases passed(20 ms)
# Your runtime beats 99.99 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
