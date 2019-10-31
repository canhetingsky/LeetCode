#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i

        return not goal
# @lc code=end

# Accepted
# 75/75 cases passed(96 ms)
# Your runtime beats 95.31 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions(15.9 MB)
