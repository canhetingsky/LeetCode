#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_closest = pow(2, 31)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_value = nums[i] + nums[l] + nums[r]
                if abs(sum_value - target) < abs(sum_closest - target):
                    sum_closest = sum_value

                if sum_value < target:
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                elif sum_value > target:
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                else:
                    return sum_value

        return sum_closest
