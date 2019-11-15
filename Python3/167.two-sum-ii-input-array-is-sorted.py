#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            another = target - numbers[i]
            if another in numbers[i+1:]:
                return [i + 1, numbers.index(another, i+1) + 1]

        return []
# @lc code=end

# Accepted
# 17/17 cases passed(2856 ms)
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.4 MB)
