#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid - 1

        return l
# @lc code=end

# Accepted
# 62/62 cases passed(56 ms)
# Your runtime beats 87.85 % of python3 submissions
# Your memory usage beats 5.97 % of python3 submissions(14.4 MB)
