#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = nums[:]
        for i in range(2, len(dp)):
            dp[i] += max(dp[i - 2], dp[i - 1] - nums[i - 1])

        return max(dp)
# @lc code=end

# Accepted
# 69/69 cases passed (32 ms)
# Your runtime beats 88.07 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
