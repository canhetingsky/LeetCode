#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            string = haystack[i:i + needle_len]
            if string == needle:
                return i

        return -1
# @lc code=end

# Accepted
# 74/74 cases passed(36 ms)
# Your runtime beats 80.5 % of python3 submissions
# Your memory usage beats 12.31 % of python3 submissions(14.1 MB)
