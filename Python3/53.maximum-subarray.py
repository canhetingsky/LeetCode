#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution:
    # Solution 2:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = nums[0]  # containing at least one number
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum

    # Solution 1:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     max_sum = nums[0]
    #     for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             max_sum = max(max_sum, sum(nums[i:j + 1]))

    #     return max_sum

    # Time Limit Exceeded
    # 199/202 cases passed(N/A)
# @lc code=end

# AcAccepted
# 202/202 cases passed(80 ms)
# Your runtime beats 53.6 % of python3 submissions
# Your memory usage beats 5.69 % of python3 submissions(14.4 MB)
