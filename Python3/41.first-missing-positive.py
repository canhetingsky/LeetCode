#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1

        return res
# @lc code=end

# Accepted
# 165/165 cases passed(44 ms)
# Your runtime beats 61.68 % of python3 submissions
# Your memory usage beats 8.7 % of python3 submissions(14 MB)
