#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start


class Solution:
    # Solution 2
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]  # the number of 0,1,2
        for num in nums:
            count[num] += 1  # take count of colors
        for i in range(count[0]):
            nums[i] = 0
        for i in range(count[0], count[0] + count[1]):
            nums[i] = 1
        for i in range(count[0]+count[1], len(nums)):
            nums[i] = 2

    # Solution 1
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()
    # Accepted
    # 87/87 cases passed(28 ms)
    # Your runtime beats 99.71 % of python3 submissions
    # Your memory usage beats 100 % of python3 submissions(12.8 MB)
# @lc code=end

# Accepted
# 87/87 cases passed(32 ms)
# Your runtime beats 97.91 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
