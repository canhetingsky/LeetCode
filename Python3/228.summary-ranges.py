#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]  # the first start number
        index = 1

        def info(start: int, end: int):
            if start == end:  # sorted integer array without duplicates
                return str(start)
            else:
                return "{0}->{1}".format(start, end)

        while index < len(nums):
            if nums[index] - nums[index - 1] > 1:  # not continuous
                end = nums[index - 1]
                res.append(info(start, end))
                start = nums[index]
            index += 1

        end = nums[-1]  # the last end number
        res.append(info(start, end))

        return res
# @lc code=end

# Accepted
# 28/28 cases passed(28 ms)
# Your runtime beats 89.9 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
