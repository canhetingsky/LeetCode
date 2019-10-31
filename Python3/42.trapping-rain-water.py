#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1  # using 2 pointers
        l_max = r_max = 0
        while l < r:
            if height[l] < l_max:
                water += (l_max - height[l])
            if height[r] < r_max:
                water += (r_max-height[r])

            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return water
# @lc code=end

# Accepted
# 315/315 cases passed(64 ms)
# Your runtime beats 51.72 % of python3 submissions
# Your memory usage beats 6.98 % of python3 submissions(14.5 MB)
