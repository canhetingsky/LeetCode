#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                      '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n1 = n2 = 0
        for num in num1:
            n1 = n1 * 10 + digits_dic[num]
        for num in num2:
            n2 = n2 * 10 + digits_dic[num]

        return str(n1 * n2)
# @lc code=end

# Accepted
# 311/311 cases passed(32 ms)
# Your runtime beats 98.33 % of python3 submissions
# Your memory usage beats 7.14 % of python3 submissions(13.8 MB)
