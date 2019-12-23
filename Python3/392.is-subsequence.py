#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c not in t:
                return False
            index = t.index(c)
            t = t[index + 1:]

        return True
# @lc code=end

# Accepted
# 14/14 cases passed(24 ms)
# Your runtime beats 99.53 % of python3 submissions
# Your memory usage beats 26.67 % of python3 submissions(17.5 MB)
