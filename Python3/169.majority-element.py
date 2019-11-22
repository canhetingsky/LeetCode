#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = {}
        for num in nums:
            times[num] = times.get(num, 0) + 1

        # sort by time
        times = sorted(times.items(), key=lambda time: time[1], reverse=True)

        return times[0][0]
# @lc code=end

# Accepted
# 44/44 cases passed(176 ms)
# Your runtime beats 97.12 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14 MB)
