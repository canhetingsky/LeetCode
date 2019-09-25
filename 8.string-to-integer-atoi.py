#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        digit_str = ''
        digit_list = [str(x) for x in range(10)]
        positive = True

        start = False
        for c in s:
            if start:
                if c in digit_list:
                    digit_str += c
                else:
                    break
            else:
                if c != ' ':
                    if c == '-':
                        positive = False
                        start = True
                    elif c == '+':
                        positive = True
                        start = True
                    elif c in digit_list:
                        start = True
                        digit_str += c
                    else:
                        return 0

        if len(digit_str) == 0:
            return 0

        if positive:
            y = int(digit_str)
        else:
            y = -int(digit_str)

        max_value = pow(2, 31) - 1
        min_value = -pow(2, 31)
        if min_value <= y <= max_value:
            return y
        elif y < min_value:
            return min_value
        else:
            return max_value
