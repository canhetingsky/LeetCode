#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(k):
                if i + j + 1 >= len(nums):
                    break
                if nums[i + j + 1] == nums[i]:
                    return True

        return False
# @lc code=end

# Time Limit Exceeded
# 22/23 cases passed(N/A)
