#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        for n1 in nums1:
            for n2 in nums2:
                res.append([n1, n2])

        res.sort(key=lambda x: sum(x))
        return res[:k]
# @lc code=end

# Accepted
# 27/27 cases passed(372 ms)
# Your runtime beats 18.27 % of python3 submissions
# Your memory usage beats 22.22 % of python3 submissions(45.8 MB)
