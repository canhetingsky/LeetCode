#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # two distinct indices i and j in the array
        # therefore, k > 0
        if k == 0:
            return False

        for i in range(len(nums) - 1):
            # the absolute difference between i and j is at most k
            # s_range = list(range(nums[i] - t, nums[i] + t + 1))
            end = min(len(nums), i + k + 1)
            for j in range(i + 1, end):
                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False
# @lc code=end

# Time Limit Exceeded
# 40/41 cases passed(N/A)
