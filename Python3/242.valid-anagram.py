#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i], 0) + 1
            letters[t[i]] = letters.get(t[i], 0) - 1

        # if t is an anagram of s, all value in letters should be 0
        for val in letters.values():
            if val != 0:
                return False

        return True
# @lc code=end

# Accepted
# 34/34 cases passed(60 ms)
# Your runtime beats 56.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13 MB)
