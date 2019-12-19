#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_list = list(magazine)
        for s in ransomNote:
            if s not in magazine_list:
                return False
            magazine_list.remove(s)

        return True
# @lc code=end

# Accepted
# 126/126 cases passed(60 ms)
# Your runtime beats 55.4 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.1 MB)
