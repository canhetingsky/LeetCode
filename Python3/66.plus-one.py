#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits))[::-1]:
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.insert(0, 1)
        return digits
# @lc code=end

# Accepted
# 109/109 cases passed(32 ms)
# Your runtime beats 97.03 % of python3 submissions
# Your memory usage beats 5.13 % of python3 submissions(13.8 MB)
