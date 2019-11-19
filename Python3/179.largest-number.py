#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums))[::-1]:
            for j in range(i):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        largest_num = ''.join(map(str, nums))
        return '0' if largest_num[0] == '0' else largest_num

    def compare(self, x, y):
        return str(x) + str(y) > str(y) + str(x)
# @lc code=end

# Accepted
# 222/222 cases passed(116 ms)
# Your runtime beats 6.87 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.7 MB)
