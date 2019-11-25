#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1, 10))  # numbers from 1 to 9
        res = []
        self.k = k
        self.dfs(candidates, n, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            if len(path) == self.k:
                res.append(path)
            return
        if len(path) >= self.k:
            return
        for i in range(index, len(nums)):
            # each combination should be a unique set of numbers
            self.dfs(nums, target-nums[i], i + 1, path+[nums[i]], res)
# @lc code=end

# Accepted
# 18/18 cases passed(24 ms)
# Your runtime beats 98.82 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions(12.6 MB)
