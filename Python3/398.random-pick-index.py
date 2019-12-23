#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        # find all index of target in nums
        index = [i for i in range(len(self.nums)) if self.nums[i] == target]
        return random.choice(index)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

# Accepted
# 13/13 cases passed(312 ms)
# Your runtime beats 88.85 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions(16.7 MB)
