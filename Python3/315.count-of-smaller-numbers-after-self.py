#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            if i < len(nums)-1:
                count = len(
                    list(filter(lambda num: num < nums[i], nums[i+1:])))
            else:
                count = 0
            res.append(count)

        return res
# @lc code=end

# Time Limit Exceeded
# 15/16 cases passed(N/A)
