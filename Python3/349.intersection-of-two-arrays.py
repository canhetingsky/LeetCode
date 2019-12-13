#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num not in res and num in nums2:
                res.append(num)

        return res
# @lc code=end

# Accepted
# 60/60 cases passed(64 ms)
# Your runtime beats 22.66 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
