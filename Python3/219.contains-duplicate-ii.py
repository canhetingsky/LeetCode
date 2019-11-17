#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, val in enumerate(nums):
            if val in dic and index - dic[val] <= k:
                return True
            dic[val] = index

        return False
# @lc code=end

# Accepted
# 23/23 cases passed(96 ms)
# Your runtime beats 96.12 % of python3 submissions
# Your memory usage beats 62.5 % of python3 submissions(20.5 MB)
