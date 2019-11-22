#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        quo, rem = divmod(abs(numerator), abs(denominator))
        integer_part = '-' + str(quo) if numerator * \
            denominator < 0 else str(quo)
        if rem == 0:  # no fractional part
            return integer_part

        res = []
        stack = []
        while rem not in stack:
            stack.append(rem)
            quo, rem = divmod(rem * 10, abs(denominator))
            res.append(str(quo))
            if rem == 0:  # the fractional part isn't repeating
                break
        else:
            # the fractional part is repeating
            index = stack.index(rem)
            res.insert(index, '(')
            res.append(')')

        return integer_part + '.' + ''.join(res)
# @lc code=end

# Accepted
# 37/37 cases passed (28 ms)
# Your runtime beats 94.81 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
