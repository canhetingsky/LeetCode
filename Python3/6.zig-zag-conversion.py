#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s

        list_str = ['']*numRows
        index, step = 0, 1
        for c in s:
            list_str[index] += c
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        new_s = ''.join(list_str)

        return new_s
