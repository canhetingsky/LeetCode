#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
# @lc code=end

# Accepted
# 21/21 cases passed(44 ms)
# Your runtime beats 97.76 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14 MB)
