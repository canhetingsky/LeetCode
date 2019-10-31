#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


class Solution:
    def reverse(self, x: int) -> int:
        max_value = pow(2, 31) - 1
        min_value = -pow(2, 31)

        if x > 0:
            positive = True
        elif x < 0:
            positive = False
            x = -x
        else:
            return x

        x_str = str(x)
        y_str = x_str[::-1]
        zero_count = 0
        while True:
            if y_str[zero_count] == '0':
                zero_count += 1
            else:
                break

        if positive:
            y = int(y_str[zero_count:])
        else:
            y = -int(y_str[zero_count:])

        if min_value <= y <= max_value:
            return y
        else:
            return 0
