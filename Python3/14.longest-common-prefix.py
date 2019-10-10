#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        str_zipped = zip(*strs)
        for c in str_zipped:
            if len(set(c)) > 1:
                break
            prefix += c[0]
        return prefix
