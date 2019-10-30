#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in sorted(strs):
            key = tuple(sorted(s))
            anagrams[key] = anagrams.get(key, []) + [s]
        return anagrams.values()
# @lc code=end

# Accepted
# 101/101 cases passed(120 ms)
# Your runtime beats 48.48 % of python3 submissions
# Your memory usage beats 30.19 % of python3 submissions(17.7 MB)
