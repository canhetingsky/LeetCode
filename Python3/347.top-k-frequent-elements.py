#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for i in range(len(nums)):
            frequent[nums[i]] = frequent.get(nums[i], 0) + 1
        frequentSortList = sorted(
            frequent.items(), key=lambda x: x[1], reverse=True)  # sorted by value
        elements = []
        for i in range(k):
            elements.append(frequentSortList[i][0])

        return elements
# @lc code=end

# Accepted
# 21/21 cases passed(108 ms)
# Your runtime beats 83.47 % of python3 submissions
# Your memory usage beats 6.25 % of python3 submissions(17.5 MB)
