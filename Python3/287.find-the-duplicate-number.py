#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start


class Solution:
    # Solution 2
    def findDuplicate(self, nums: List[int]) -> int:
        # there is only one duplicate number in the array
        # the duplicate number could be repeated more than once
        res = []
        for num in nums:
            if num in res:
                return num
            res.append(num)

    # Solution 1
    # def findDuplicate(self, nums: List[int]) -> int:
    #     return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))
    # Accepted
    # 53/53 cases passed(64 ms)
    # Your runtime beats 96.22 % of python3 submissions
    # Your memory usage beats 7.14 % of python3 submissions(16.7 MB)
# @lc code=end

# Accepted
# 53/53 cases passed(2236 ms)
# Your runtime beats 5.16 % of python3 submissions
# Your memory usage beats 21.43 % of python3 submissions(15.1 MB)
