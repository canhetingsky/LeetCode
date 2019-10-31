#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        last_num = nums[-1]
        pre_nums = nums[:-1]
        permutations = []
        pre_permutations = self.permuteUnique(pre_nums)  # backtracking
        for p in pre_permutations:
            for i in range(len(p)):
                temp = p.copy()
                temp.insert(i, last_num)
                if temp not in permutations:  # only add unique permutations
                    permutations.append(temp)
            temp = p + [last_num]
            if temp not in permutations:  # only add unique permutations
                permutations.append(temp)

        return permutations
# @lc code=end

# Accepted
# 30/30 cases passed(100 ms)
# Your runtime beats 30.49 % of python3 submissions
# Your memory usage beats 8.89 % of python3 submissions(13.9 MB)
