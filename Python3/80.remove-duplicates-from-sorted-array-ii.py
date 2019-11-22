#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        index = 2

        while index < len(nums):
            if nums[index] == nums[index - 1] and nums[index] == nums[index - 2]:
                nums.pop(index)
            else:
                index += 1

        return len(nums)
# @lc code=end

# Accepted
# 166/166 cases passed(52 ms)
# Your runtime beats 99.65 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
