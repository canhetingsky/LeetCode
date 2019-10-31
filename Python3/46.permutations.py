#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        last_num = nums[-1]
        pre_nums = nums[:-1]
        permutations = []
        pre_permutations = self.permute(pre_nums)  # backtracking
        for p in pre_permutations:
            for i in range(len(p)):
                temp = p.copy()
                temp.insert(i, last_num)
                permutations.append(temp)
            temp = p + [last_num]
            permutations.append(temp)

        return permutations
# @lc code=end

# Accepted
# 25/25 cases passed(44 ms)
# Your runtime beats 91.12 % of python3 submissions
# Your memory usage beats 5.36 % of python3 submissions(13.9 MB)
