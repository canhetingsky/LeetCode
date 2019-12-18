#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        dp = {}

        def dp_recur(nums, target, dp):
            if target in dp:
                return dp[target]
            else:
                count = 0
                for num in nums:
                    if num <= target:
                        new_target = target - num
                        if new_target == 0:
                            count += 1
                            continue
                        count += dp_recur(nums, new_target, dp)

                dp[target] = count
            return count

        return dp_recur(nums, target, dp)
# @lc code=end

# Accepted
# 17/17 cases passed(36 ms)
# Your runtime beats 97.26 % of python3 submissions
# Your memory usage beats 22.22 % of python3 submissions(16.5 MB)
