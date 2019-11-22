#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        #filter alphanumeric and characters 
        #convert characters to lowercase
        s = ''.join(list(filter(str.isalnum, s))).lower()

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
# @lc code=end

# Accepted
# 476/476 cases passed (36 ms)
# Your runtime beats 99.33 % of python3 submissions
# Your memory usage beats 65.48 % of python3 submissions (13.5 MB)
