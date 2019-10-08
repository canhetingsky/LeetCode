#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        max_length = 0

        for i in range(len_s):
            if i + max_length >= len_s:
                return max_length

            list_add = []
            for j in range(i, len_s):
                if s[j] in list_add:
                    break
                list_add.append(s[j])

            max_length = max(max_length, len(list_add))

        return max_length
