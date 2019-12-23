#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for key, value in count.items():
            if value == 1:
                return s.index(key)

        return -1
# @lc code=end

# Accepted
# 104/104 cases passed(116 ms)
# Your runtime beats 62.85 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
