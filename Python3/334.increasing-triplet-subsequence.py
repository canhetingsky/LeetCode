#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = pow(2, 31)  # max int value
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # first <num <= second
                second = num
            else:  # num > second > first
                return True
        return False
# @lc code=end

# Accepted
# 62/62 cases passed(64 ms)
# Your runtime beats 56.27 % of python3 submissions
# Your memory usage beats 88.89 % of python3 submissions(13.4 MB)
