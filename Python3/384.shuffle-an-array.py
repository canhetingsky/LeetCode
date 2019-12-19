#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        new_nums = self.nums[:]
        random.shuffle(new_nums)
        return new_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

# Accepted
# 10/10 cases passed(276 ms)
# Your runtime beats 95.55 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(18 MB)
