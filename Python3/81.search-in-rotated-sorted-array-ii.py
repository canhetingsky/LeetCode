#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = l + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = r - 1

        return False
# @lc code=end

# Accepted
# 275/275 cases passed(52 ms)
# Your runtime beats 99.69 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.2 MB)
