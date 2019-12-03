#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums)/3

        elements = set(nums)

        res = [num for num in elements if nums.count(num) > times]

        return res
# @lc code=end

# Accepted
# 66/66 cases passed(116 ms)
# Your runtime beats 98.31 % of python3 submissions
# Your memory usage beats 29.41 % of python3 submissions(14 MB)
