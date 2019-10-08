#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        if len(nums) < 4:
            return []

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        array = [nums[i], nums[j], nums[l], nums[r]]
                        if array not in res:
                            res.append(array)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1

        return res
# @lc code=end
