#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start


class Solution:
    # Solution 2
    def toHex(self, num: int) -> str:
        if num < 0:
            num = 0xffffffff + 1 + num
        return str(hex(num)).replace('0x','')

    # Solution 1
    # def toHex(self, num: int) -> str:
    #     ch = ['0', '1', '2', '3', '4', '5', '6',
    #           '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    #     hex_str = ""
    #     if num == 0:
    #         return '0'
    #     if num < 0:
    #         num = 0xffffffff + 1 + num
    #     while num > 0:
    #         num, rem = divmod(num, 16)
    #         hex_str = ch[rem]+hex_str

    #     return hex_str
    # Accepted
    # 100/100 cases passed (28 ms)
    # Your runtime beats 76.26 % of python3 submissions
    # Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=end

# Accepted
# 100/100 cases passed (24 ms)
# Your runtime beats 91.1 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
