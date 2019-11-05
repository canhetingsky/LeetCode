#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(map(int, a)), list(map(int, b))
        i, j = len(a) - 1, len(b) - 1  # the input strings are both non-empty
        sum_str = ''
        carry = 0
        while i >= 0 and j >= 0:
            value = a[i] + b[j] + carry
            if value >= 2:
                sum_str += str(value % 2)
                carry = value // 2
            else:
                sum_str += str(value)
                carry = 0
            i -= 1
            j -= 1

        while i >= 0:
            value = a[i] + carry
            if value >= 2:
                sum_str += str(value % 2)
                carry = value // 2
            else:
                sum_str += str(value)
                carry = 0
            i -= 1

        while j >= 0:
            value = b[j] + carry
            if value >= 2:
                sum_str += str(value % 2)
                carry = value // 2
            else:
                sum_str += str(value)
                carry = 0
            j -= 1

        if carry > 0:
            sum_str += '1'
        return sum_str[::-1]
# @lc code=end

# Accepted
# 294/294 cases passed(40 ms)
# Your runtime beats 73.72 % of python3 submissions
# Your memory usage beats 5.41 % of python3 submissions(13.7 MB)
