#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if the array contains any duplicates,
        # the length of nums and set(nums) are not equal,
        # so return true
        return len(nums) != len(set(nums))
# @lc code=end

# Accepted
# 18/18 cases passed(108 ms)
# Your runtime beats 99.98 % of python3 submissions
# Your memory usage beats 88.68 % of python3 submissions(17.9 MB)
