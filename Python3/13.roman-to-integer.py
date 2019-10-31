#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        num = 0
        for c in s:
            num += symbols.get(c)
        return num
