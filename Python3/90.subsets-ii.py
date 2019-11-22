#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for num in nums:
            subsets = res[:]  # back tracking
            for subset in subsets:
                subset = subset + [num]
                if subset not in res:
                    res.append(subset)

        return res
# @lc code=end

# Accepted
# 19/19 cases passed(36 ms)
# Your runtime beats 98.22 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
