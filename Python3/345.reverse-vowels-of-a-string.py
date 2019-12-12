#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        list_s = list(s)  # convert str to list
        l, r = 0, len(list_s) - 1  # two pointers
        while l < r:
            if list_s[l] not in vowels and list_s[r] in vowels:
                l += 1
            elif list_s[l] in vowels and list_s[r] not in vowels:
                r -= 1
            else:
                if list_s[l] in vowels and list_s[r] in vowels:
                    # list items can swap
                    list_s[l], list_s[r] = list_s[r], list_s[l]
                l += 1
                r -= 1

        return ''.join(list_s)
# @lc code=end

# Accepted
# 481/481 cases passed(68 ms)
# Your runtime beats 43.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.6 MB)
