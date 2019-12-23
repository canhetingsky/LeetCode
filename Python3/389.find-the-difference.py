#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = list(t)
        for c in s:
            res.remove(c)

        return ''.join(res)
# @lc code=end

# Accepted
# 54/54 cases passed(44 ms)
# Your runtime beats 36.1 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
