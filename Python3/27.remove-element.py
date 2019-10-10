#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                index -= 1
            index += 1

        return len(nums)
# @lc code=end

# Accepted
# 113/113 cases passed(44 ms)
# Your runtime beats 32.07 % of python3 submissions
# Your memory usage beats 6.06 % of python3 submissions(13.8 MB)
