#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0

        return len(words[-1])
# @lc code=end

# Accepted
# 59/59 cases passed(40 ms)
# Your runtime beats 33.11 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions(13.9 MB)
