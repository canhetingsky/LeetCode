#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key
# @lc code=end

# Accepted
# 16/16 cases passed(92 ms)
# Your runtime beats 93.36 % of python3 submissions
# Your memory usage beats 19.67 % of python3 submissions(15.1 MB)
