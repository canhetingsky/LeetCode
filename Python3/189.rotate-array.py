#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            num = nums.pop()
            nums.insert(0, num)
# @lc code=end

# Accepted
# 34/34 cases passed(136 ms)
# Your runtime beats 20.16 % of python3 submissions
# Your memory usage beats 5.09 % of python3 submissions(14 MB)
