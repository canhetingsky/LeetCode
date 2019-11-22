#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    # Solution 1
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     for i in range(k):  # bubble sort
    #         for j in range(len(nums) - i - 1):
    #             if nums[j] > nums[j + 1]:
    #                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
    #     return nums[-k]
    # Accepted
    # 32/32 cases passed(5372 ms)
    # Your runtime beats 5.03 % of python3 submissions
    # Your memory usage beats 100 % of python3 submissions(13.5 MB)
# @lc code=end

# Accepted
# 32/32 cases passed(64 ms)
# Your runtime beats 96.43 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(13.3 MB)
