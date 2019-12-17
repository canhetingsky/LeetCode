#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        val = 0
        for num in b:
            val = val * 10 + num

        return pow(a, val, 1337)
# @lc code=end

# Accepted
# 54/54 cases passed(88 ms)
# Your runtime beats 95.89 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.8 MB)
