#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                area = max(area, h * w)
            stack.append(i)

        return area
# @lc code=end

# Accepted
# 96/96 cases passed(104 ms)
# Your runtime beats 98.69 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(14.4 MB)
