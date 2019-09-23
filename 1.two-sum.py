#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            another = target - nums[i]
            if another in nums[i+1:]:
                return [i, nums.index(another, i+1)]

        return []
