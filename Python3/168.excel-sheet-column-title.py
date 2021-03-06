#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start


class Solution:
    def convertToTitle(self, n: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while n > 0:
            result.append(capitals[(n-1) % 26])
            n = (n-1) // 26
        result.reverse()

        return ''.join(result)
# @lc code=end

# Accepted
# 18/18 cases passed(24 ms)
# Your runtime beats 98.41 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
