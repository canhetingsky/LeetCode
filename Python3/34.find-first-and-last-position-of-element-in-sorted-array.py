#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        l_index = r_index = -1

        while l <= r:
            if nums[l] == target:
                l_index = l
            else:
                l += 1

            if nums[r] == target:
                r_index = r
            else:
                r -= 1

            if l_index != -1 and r_index != -1:
                break

        return [l_index, r_index]
# @lc code=end

# Accepted
# 88/88 cases passed(108 ms)
# Your runtime beats 19.86 % of python3 submissions
# Your memory usage beats 5.36 % of python3 submissions(15 MB)
