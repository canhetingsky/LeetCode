#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        digist = {}
        for num in nums:
            digist[num] = digist.get(num, 0) + 1

        res = [num for num in digist.keys() if digist[num] == 1]
        return res
# @lc code=end

# Accepted
# 30/30 cases passed(56 ms)
# Your runtime beats 97.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.4 MB)
