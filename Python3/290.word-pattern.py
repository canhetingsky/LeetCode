#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word = str.split()
        if len(pattern) != len(word):
            return False

        match = {}
        for i in range(len(pattern)):
            if pattern[i] not in match.keys():
                if word[i] in match.values():
                    return False
                match[pattern[i]] = word[i]  # add key and value to match
            elif word[i] != match[pattern[i]]:
                return False

        return True
# @lc code=end

# Accepted
# 33/33 cases passed(28 ms)
# Your runtime beats 88.2 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
