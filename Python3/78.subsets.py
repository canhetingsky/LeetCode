#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [pre + [num] for pre in res]

        return res
# @lc code=end

# Accepted
# 10/10 cases passed(32 ms)
# Your runtime beats 98.95 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.9 MB)
