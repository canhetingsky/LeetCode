#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num not in res and num in nums2:
                time = min(nums1.count(num), nums2.count(num))
                res += [num] * time

        return res
# @lc code=end

# Accepted
# 61/61 cases passed(88 ms)
# Your runtime beats 5.96 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
