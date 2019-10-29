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
            elif num > res:
                break

        return res
# @lc code=end

# Accepted
# 165/165 cases passed(40 ms)
# Your runtime beats 86.9 % of python3 submissions
# Your memory usage beats 8.7 % of python3 submissions(13.7 MB)
