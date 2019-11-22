#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
            
        length = -1
        sum_val = 0
        left =0
        for i in range(len(nums)):
            sum_val += nums[i]
            while sum_val >= s:
                if length == -1:
                    length = i - left + 1
                else:
                    length = min(length, i - left + 1)
                sum_val -= nums[left]
                left +=1

        return length if length != -1 else 0
# @lc code=end

# Accepted
# 15/15 cases passed(80 ms)
# Your runtime beats 89.36 % of python3 submissions
# Your memory usage beats 7.69 % of python3 submissions(15.3 MB)
