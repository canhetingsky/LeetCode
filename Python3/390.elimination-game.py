#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#

# @lc code=start


class Solution:
    def lastRemaining(self, n: int) -> int:
        def remain(nums: List[int]) -> List[int]:
            if len(nums) == 1:
                return nums
            new_nums = nums[1: len(nums):2]
            new_nums.reverse()
            return remain(new_nums)

        nums = list(range(1, n + 1))
        return remain(nums)[0]
# @lc code=end

# Memory Limit Exceeded
# 3375/3377 cases passed(N/A)
# Testcase
# 100000000
