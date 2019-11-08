#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        nums1[m:m + n] = nums2[:]
        nums1.sort()
# @lc code=end

# Accepted
# 59/59 cases passed(36 ms)
# Your runtime beats 97.87 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
