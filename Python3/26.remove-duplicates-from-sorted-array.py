#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                del nums[index]
                index -= 1
            index += 1
        return len(nums)
# @lc code=end

# Accepted
# 161/161 cases passed(120 ms)
# Your runtime beats 16.21 % of python3 submissions
# Your memory usage beats 5.74 % of python3 submissions(15.4 MB)
