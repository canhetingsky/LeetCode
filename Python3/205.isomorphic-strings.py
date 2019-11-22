#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss, tt = {}, {}
        for i in range(len(s)):  # map s to t ,map t to s
            if s[i] not in ss:
                ss[s[i]] = t[i]
            elif ss[s[i]] is not t[i]:
                return False

            if t[i] not in tt:
                tt[t[i]] = s[i]
            elif tt[t[i]] is not s[i]:
                return False

        return True
# @lc code=end

# Accepted
# 30/30 cases passed(36 ms)
# Your runtime beats 96.83 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.9 MB)
