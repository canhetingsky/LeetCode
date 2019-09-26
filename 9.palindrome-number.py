#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        origin_str = str(x)
        new_str = origin_str[::-1]
        if new_str == origin_str:
            return True
        else:
            return False
