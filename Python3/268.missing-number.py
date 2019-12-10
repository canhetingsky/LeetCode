#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:  # find missing number
                return nums[i] + 1

        max_val = max(nums)
        if max_val >= len(nums):
            return nums[0] - 1
        else:
            return nums[-1] + 1
# @lc code=end

# Accepted
# 122/122 cases passed(152 ms)
# Your runtime beats 72.32 % of python3 submissions
# Your memory usage beats 95.16 % of python3 submissions(13.9 MB)
