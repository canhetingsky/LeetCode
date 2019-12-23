#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1, n+1), key=str)
# @lc code=end

# Accepted
# 26/26 cases passed(96 ms)
# Your runtime beats 98.05 % of python3 submissions
# Your memory usage beats 50 % of python3 submissions(19.4 MB)
