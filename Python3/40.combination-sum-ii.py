#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            if path not in res:  # exclude duplicate combinations
                res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i + 1, path+[nums[i]], res)
# @lc code=end

# Accepted
# 172/172 cases passed(528 ms)
# Your runtime beats 10.72 % of python3 submissions
# Your memory usage beats 6.52 % of python3 submissions(13.7 MB)
